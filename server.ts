import express from "express";
import path from "path";
import { createServer as createViteServer } from "vite";
import { GoogleGenAI } from "@google/genai";
import fs from "fs/promises";

// Initialize Gemini Client
const ai = new GoogleGenAI({ 
    apiKey: process.env.GEMINI_API_KEY,
    httpOptions: {
        headers: {
            'User-Agent': 'aistudio-build'
        }
    }
});

const app = express();
const PORT = 3000;

app.use(express.json());

// 1. AI Tutor Chat Endpoint
app.post("/api/chat", async (req, res) => {
    try {
        const { message, history } = req.body;
        
        const chat = ai.chats.create({
            model: "gemini-3.7-flash",
            config: {
                systemInstruction: "You are a helpful, encouraging, and knowledgeable AI Tutor. You explain concepts clearly, provide examples, and ask guiding questions to help students learn.",
            },
        });

        // Initialize chat history if provided
        if (history && Array.isArray(history)) {
            for (const turn of history) {
                await chat.sendMessage({ message: turn.parts[0].text }); // Simple simulation of history, though ideally we'd pass history to chat initialization
            }
        }

        const streamResponse = await chat.sendMessageStream({ message });
        
        res.setHeader('Content-Type', 'text/event-stream');
        res.setHeader('Cache-Control', 'no-cache');
        res.setHeader('Connection', 'keep-alive');

        for await (const chunk of streamResponse) {
            if (chunk.text) {
                res.write(`data: ${JSON.stringify({ text: chunk.text })}\n\n`);
            }
        }
        res.write('data: [DONE]\n\n');
        res.end();
    } catch (error: any) {
        console.error("Chat error:", error);
        res.status(500).json({ error: error.message });
    }
});

// 2. Start Deep Research Endpoint
app.post("/api/research/start", async (req, res) => {
    try {
        const { query } = req.body;
        const interaction = await ai.interactions.create({
            agent: "deep-research-preview-04-2026",
            input: `Research the following topic thoroughly: ${query}. Provide a comprehensive markdown report with citations, facts, and structure.`,
            background: true,
        });
        res.json({ interactionId: interaction.id });
    } catch (error: any) {
        console.error("Research start error:", error);
        res.status(500).json({ error: error.message });
    }
});

// 3. Poll Deep Research Status
app.get("/api/research/status/:id", async (req, res) => {
    try {
        const interactionId = req.params.id;
        const queryName = req.query.name as string || "research";
        
        const interaction = await ai.interactions.get(interactionId);
        
        if (interaction.status === "completed") {
            let fullReport = "";
            for (const step of interaction.steps) {
                if (step.type === 'model_output') {
                    const textContent = step.content?.find(c => c.type === 'text');
                    if (textContent && textContent.text) {
                        fullReport += textContent.text;
                    }
                }
            }
            
            // Save to file
            const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
            const safeName = queryName.replace(/[^a-z0-9]/gi, '_').substring(0, 30);
            const filename = `${safeName}_${timestamp}.md`;
            const filepath = path.join(process.cwd(), 'public', 'research', filename);
            
            await fs.writeFile(filepath, fullReport, 'utf8');
            
            res.json({ status: "completed", filename, report: fullReport });
        } else if (["failed", "cancelled"].includes(interaction.status)) {
            res.json({ status: interaction.status });
        } else {
            res.json({ status: "running" });
        }
    } catch (error: any) {
        console.error("Research status error:", error);
        res.status(500).json({ error: error.message });
    }
});

// 4. List Research Files
app.get("/api/research/files", async (req, res) => {
    try {
        const researchDir = path.join(process.cwd(), 'public', 'research');
        const files = await fs.readdir(researchDir);
        const mdFiles = files.filter(f => f.endsWith('.md'));
        res.json({ files: mdFiles });
    } catch (error: any) {
        console.error("List files error:", error);
        res.status(500).json({ error: error.message });
    }
});

// 5. Read Research File
app.get("/api/research/file/:name", async (req, res) => {
    try {
        const filename = req.params.name;
        // Basic security check to prevent directory traversal
        if (filename.includes('..') || filename.includes('/')) {
            return res.status(400).json({ error: "Invalid filename" });
        }
        const filepath = path.join(process.cwd(), 'public', 'research', filename);
        const content = await fs.readFile(filepath, 'utf8');
        res.json({ content });
    } catch (error: any) {
        console.error("Read file error:", error);
        res.status(500).json({ error: error.message });
    }
});

async function startServer() {
    // Vite middleware for development
    if (process.env.NODE_ENV !== "production") {
        const vite = await createViteServer({
            server: { middlewareMode: true },
            appType: "spa",
        });
        app.use(vite.middlewares);
    } else {
        const distPath = path.join(process.cwd(), 'dist');
        app.use(express.static(distPath));
        app.get('*', (req, res) => {
            res.sendFile(path.join(distPath, 'index.html'));
        });
    }

    app.listen(PORT, "0.0.0.0", () => {
        console.log(`Server running on http://localhost:${PORT}`);
    });
}

startServer();
