# Cloud Architect Academy

An interactive, AI-powered eLearning platform designed to teach Cloud Architecture, Infrastructure as Code (IaC), and domain-specific specializations like MLOps and Data Engineering.

This application features native AI integrations:
- **AI Tutor**: An interactive, streaming chatbot powered by Gemini to answer complex architectural questions.
- **Deep Research Agent**: An autonomous agent that browses the web to generate comprehensive markdown reports on cloud topics.

## Prerequisites
- Node.js (v18 or higher)
- A Gemini API Key from Google AI Studio

## Local Setup & Configuration

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Set up Environment Variables**:
   Copy the example environment file and add your API key.
   ```bash
   cp .env.example .env
   ```
   Open `.env` and securely configure your `GEMINI_API_KEY`:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```

4. **Run the Development Server**:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:3000`.

## Architecture & Data
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript, Marked.js (for markdown rendering).
- **Backend**: Express.js server (in `server.ts`) for secure API proxying and local file system management.
- **Content DB**: Static course data and curriculum information is served natively from `public/data.json`.
- **Research Artifacts**: Dynamically generated markdown reports from the Deep Research agent are saved natively to the `public/research/` directory.

## Integrating with other AI Agents
Because this application uses a modular, local file-system approach (`data.json` for content and `/research/*.md` for output), other AI agentic tools (like AutoGPT, Devin, or custom scripts) can seamlessly interact with it by simply reading/writing to the `public/` directory without needing a database connection.
