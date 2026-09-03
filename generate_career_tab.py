import json

html = """
            <div id="tab-career" class="tab-content hidden fade-in">
                <!-- Header -->
                <header class="mb-10 text-center">
                    <div class="text-[10px] font-bold text-emerald-500 uppercase tracking-widest mb-1">Career Development</div>
                    <h2 class="text-3xl font-bold text-white mb-4">Global Cloud Infrastructure Market (2026)</h2>
                    <p class="text-sm text-slate-400 max-w-4xl mx-auto leading-relaxed">
                        AWS, Azure, and Google Cloud dominate the global cloud infrastructure market [24], collectively controlling approximately 63% of the total industry [26]. While cloud spending continues to accelerate rapidly—reaching $99 billion in a single quarter of 2025 (a 25% year-over-year increase) [25]—a massive cloud skills gap remains, keeping cloud certifications among the most valuable and highest-paying IT assets globally [27].
                    </p>
                </header>

                <!-- Hyperscalers -->
                <div class="mb-12">
                    <h3 class="text-lg font-bold text-white mb-6 border-b border-slate-800 pb-2">Top Hyperscalers</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <!-- AWS -->
                        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 hover:border-orange-500 transition-colors relative overflow-hidden group">
                            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                                <i class="fa-brands fa-aws text-6xl text-orange-500"></i>
                            </div>
                            <h4 class="text-xl font-bold text-white mb-1">AWS</h4>
                            <div class="text-xs text-orange-400 font-bold mb-4">30% - 32% Market Share</div>
                            <ul class="space-y-3 relative z-10">
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Known For</span> Largest ecosystem, mature services, startup and enterprise adoption.</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Ecosystem</span> 200+ fully featured cloud services.</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Average Salary</span> $135,000</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Demand</span> 180,000+ US jobs (+15% growth)</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Ideal For</span> Startups, SaaS platforms, tech companies, general default path.</li>
                            </ul>
                        </div>
                        <!-- Azure -->
                        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 hover:border-blue-500 transition-colors relative overflow-hidden group">
                            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                                <i class="fa-brands fa-microsoft text-6xl text-blue-500"></i>
                            </div>
                            <h4 class="text-xl font-bold text-white mb-1">Azure</h4>
                            <div class="text-xs text-blue-400 font-bold mb-4">20% - 23% Market Share</div>
                            <ul class="space-y-3 relative z-10">
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Known For</span> Enterprise integration, hybrid cloud, Microsoft corporate IT.</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Ecosystem Focus</span> Windows Server, Active Directory, SQL Server, Office 365.</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Average Salary</span> $130,000</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Demand</span> 140,000+ US jobs (+20% growth)</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Ideal For</span> Enterprise environments, Fortune 500, Microsoft partners.</li>
                            </ul>
                        </div>
                        <!-- GCP -->
                        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 hover:border-red-500 transition-colors relative overflow-hidden group">
                            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                                <i class="fa-brands fa-google text-6xl text-red-500"></i>
                            </div>
                            <h4 class="text-xl font-bold text-white mb-1">Google Cloud (GCP)</h4>
                            <div class="text-xs text-red-400 font-bold mb-4">10% - 13% Market Share</div>
                            <ul class="space-y-3 relative z-10">
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Known For</span> Data analytics, machine learning/AI models, Kubernetes.</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Ecosystem Focus</span> Open-source frameworks, BigQuery, Vertex AI.</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Average Salary</span> $140,000 (highest avg)</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Demand</span> 60,000+ US jobs (+25% growth)</li>
                                <li class="text-xs text-slate-300"><span class="font-bold text-slate-500 block mb-1">Ideal For</span> Data science, ML, advanced analytics, Google partners.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Career Paths -->
                <div class="mb-12">
                    <h3 class="text-lg font-bold text-white mb-6 border-b border-slate-800 pb-2">Core Career Paths</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <!-- Cloud Architect -->
                        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 hover:border-emerald-500 transition-colors">
                            <div class="flex items-center gap-3 mb-4">
                                <div class="w-10 h-10 rounded-lg bg-emerald-500/10 flex items-center justify-center text-emerald-400 border border-emerald-500/20">
                                    <i class="fa-solid fa-sitemap"></i>
                                </div>
                                <h4 class="font-bold text-white">Cloud Architect</h4>
                            </div>
                            <p class="text-xs text-slate-400 mb-4 leading-relaxed">Designing, building, and optimizing production environments using best-practice cloud pillars.</p>
                            <div class="mb-4">
                                <div class="text-[10px] font-bold text-emerald-500 uppercase tracking-widest mb-1">Skills</div>
                                <p class="text-xs text-slate-300 leading-relaxed">Network isolation, disaster recovery, right-sizing, cost optimization, IAM permissions.</p>
                            </div>
                            <div>
                                <div class="text-[10px] font-bold text-emerald-500 uppercase tracking-widest mb-1">5-Year Growth (AWS Track)</div>
                                <div class="text-xs text-slate-300 flex items-center gap-2"><span class="text-emerald-400">Y1</span> $85k <i class="fa-solid fa-arrow-right text-[10px] text-slate-600"></i> <span class="text-emerald-400">Y3</span> $130k <i class="fa-solid fa-arrow-right text-[10px] text-slate-600"></i> <span class="text-emerald-400">Y5</span> $165k</div>
                            </div>
                        </div>

                        <!-- DevOps / Platform -->
                        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 hover:border-sky-500 transition-colors">
                            <div class="flex items-center gap-3 mb-4">
                                <div class="w-10 h-10 rounded-lg bg-sky-500/10 flex items-center justify-center text-sky-400 border border-sky-500/20">
                                    <i class="fa-solid fa-code-branch"></i>
                                </div>
                                <h4 class="font-bold text-white">DevOps / Platform Engineer</h4>
                            </div>
                            <p class="text-xs text-slate-400 mb-4 leading-relaxed">Building continuous deployment systems, managing container frameworks, and writing IaC templates.</p>
                            <div class="mb-4">
                                <div class="text-[10px] font-bold text-sky-500 uppercase tracking-widest mb-1">Skills</div>
                                <p class="text-xs text-slate-300 leading-relaxed">Git workflows, Linux, Python/Bash, Docker/K8s, Terraform, CloudFormation, Bicep.</p>
                            </div>
                            <div>
                                <div class="text-[10px] font-bold text-sky-500 uppercase tracking-widest mb-1">Demand</div>
                                <p class="text-xs text-slate-300">Highly specialized. 40k AWS, 30k Azure, 12k GCP jobs.</p>
                            </div>
                        </div>

                        <!-- Data / AI -->
                        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 hover:border-purple-500 transition-colors">
                            <div class="flex items-center gap-3 mb-4">
                                <div class="w-10 h-10 rounded-lg bg-purple-500/10 flex items-center justify-center text-purple-400 border border-purple-500/20">
                                    <i class="fa-solid fa-brain"></i>
                                </div>
                                <h4 class="font-bold text-white">Data Engineer / AI Specialist</h4>
                            </div>
                            <p class="text-xs text-slate-400 mb-4 leading-relaxed">Ingesting raw data streams, managing analytics warehouses, and productionizing ML models/AI clusters.</p>
                            <div class="mb-4">
                                <div class="text-[10px] font-bold text-purple-500 uppercase tracking-widest mb-1">Skills</div>
                                <p class="text-xs text-slate-300 leading-relaxed">BigQuery, Azure Synapse, Redshift, ETL, serving endpoints, TensorFlow, Vertex AI, SageMaker.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Certification Tiers -->
                <div class="mb-12">
                    <h3 class="text-lg font-bold text-white mb-6 border-b border-slate-800 pb-2">Certification Tiers Roadmap</h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                        <!-- Foundational -->
                        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl hover:border-emerald-500/50 transition-colors">
                            <div class="text-xs font-bold text-emerald-400 mb-1 uppercase tracking-wider">Tier 1</div>
                            <h4 class="text-sm font-bold text-white mb-3">Foundational</h4>
                            <p class="text-[11px] text-slate-400 mb-4 h-16 overflow-hidden">Basic cloud concepts, service models, security fundamentals. Best for beginners, PMs, sales.</p>
                            <div class="space-y-2 text-[10px]">
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">AWS</span><span class="text-slate-300">Cloud Practitioner</span></div>
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">Azure</span><span class="text-slate-300">AZ-900 Fundamentals</span></div>
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">GCP</span><span class="text-slate-300">Cloud Digital Leader</span></div>
                            </div>
                        </div>
                        
                        <!-- Associate -->
                        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl hover:border-sky-500/50 transition-colors">
                            <div class="text-xs font-bold text-sky-400 mb-1 uppercase tracking-wider">Tier 2</div>
                            <h4 class="text-sm font-bold text-white mb-3">Associate</h4>
                            <p class="text-[11px] text-slate-400 mb-4 h-16 overflow-hidden">Practical cloud implementation, deploying workloads. The most career-impactful entry stage.</p>
                            <div class="space-y-2 text-[10px]">
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">AWS</span><span class="text-slate-300">Solutions Architect Assoc.</span></div>
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">Azure</span><span class="text-slate-300">AZ-104 Administrator</span></div>
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">GCP</span><span class="text-slate-300">Assoc. Cloud Engineer</span></div>
                            </div>
                        </div>

                        <!-- Professional/Expert -->
                        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl hover:border-purple-500/50 transition-colors">
                            <div class="text-xs font-bold text-purple-400 mb-1 uppercase tracking-wider">Tier 3</div>
                            <h4 class="text-sm font-bold text-white mb-3">Professional / Expert</h4>
                            <p class="text-[11px] text-slate-400 mb-4 h-16 overflow-hidden">Advanced architecture, CI/CD pipelines, multi-region setups, SRE principles, large-scale governance.</p>
                            <div class="space-y-2 text-[10px]">
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">AWS</span><span class="text-slate-300">Solutions Architect Pro</span></div>
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">Azure</span><span class="text-slate-300">AZ-305 Architect Expert</span></div>
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">GCP</span><span class="text-slate-300">Pro Cloud Architect</span></div>
                            </div>
                        </div>

                        <!-- Specialty -->
                        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl hover:border-orange-500/50 transition-colors">
                            <div class="text-xs font-bold text-orange-400 mb-1 uppercase tracking-wider">Tier 4</div>
                            <h4 class="text-sm font-bold text-white mb-3">Specialty</h4>
                            <p class="text-[11px] text-slate-400 mb-4 h-16 overflow-hidden">Deep expertise within precise domains (Security, Networking, Big Data, Machine Learning).</p>
                            <div class="space-y-2 text-[10px]">
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">AWS</span><span class="text-slate-300">Machine Learning / Security</span></div>
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">Azure</span><span class="text-slate-300">AI / Data Engineer Assoc.</span></div>
                                <div class="flex justify-between border-b border-slate-800 pb-1"><span class="text-slate-500">GCP</span><span class="text-slate-300">Pro ML Engineer</span></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Implementation Roadmap & Multi-Cloud -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
                    <!-- Roadmap -->
                    <div>
                        <h3 class="text-lg font-bold text-white mb-6 border-b border-slate-800 pb-2">Implementation Roadmap</h3>
                        <div class="space-y-4">
                            <div class="flex gap-4">
                                <div class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-emerald-500 font-bold shrink-0 text-sm">1</div>
                                <div>
                                    <h4 class="text-sm font-bold text-white">Foundations (Months 1-3)</h4>
                                    <p class="text-[11px] text-slate-400 mt-1">Linux administration, networking basics (DNS, TCP/IP, CIDR), Bash/Python, Docker, Git.</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-sky-500 font-bold shrink-0 text-sm">2</div>
                                <div>
                                    <h4 class="text-sm font-bold text-white">Associate & Portfolio (Months 4-9)</h4>
                                    <p class="text-[11px] text-slate-400 mt-1">Deploying virtual compute/containers, configuring subnets, IAM policies. Project: Hosting web app, programmatic CI/CD.</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-purple-500 font-bold shrink-0 text-sm">3</div>
                                <div>
                                    <h4 class="text-sm font-bold text-white">Advanced Architecture (Months 10-18)</h4>
                                    <p class="text-[11px] text-slate-400 mt-1">IaC engines, Kubernetes multi-cluster, SRE incident mitigation, HA systems. Target: Professional Architect Cert.</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-orange-500 font-bold shrink-0 text-sm">4</div>
                                <div>
                                    <h4 class="text-sm font-bold text-white">Specialization (Months 18-24)</h4>
                                    <p class="text-[11px] text-slate-400 mt-1">Differentiate yourself in Cloud Security, DevOps, Big Data Pipelines, or MLOps.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Multi-Cloud & Industries -->
                    <div>
                        <h3 class="text-lg font-bold text-white mb-6 border-b border-slate-800 pb-2">Multi-Cloud Strategy</h3>
                        <div class="bg-slate-900 border border-slate-800 p-6 rounded-2xl mb-6">
                            <p class="text-xs text-slate-400 leading-relaxed mb-4">
                                <strong class="text-emerald-400">85% of enterprises operate multi-cloud environments.</strong> 
                                Multi-certified engineers earn 15-20% more and isolate themselves from platform-specific career risks. 42%+ of jobs request 2+ cloud systems.
                            </p>
                            <h4 class="text-xs font-bold text-white uppercase tracking-wider mb-3">Service Equivalents</h4>
                            <table class="w-full text-[10px] text-left">
                                <thead class="text-slate-500 border-b border-slate-800">
                                    <tr><th class="pb-2">Resource</th><th class="pb-2">AWS</th><th class="pb-2">Azure</th><th class="pb-2">GCP</th></tr>
                                </thead>
                                <tbody class="text-slate-300">
                                    <tr class="border-b border-slate-800/50"><td class="py-2">Compute</td><td class="py-2">EC2</td><td class="py-2">Virtual Machines</td><td class="py-2">Compute Engine</td></tr>
                                    <tr class="border-b border-slate-800/50"><td class="py-2">Storage</td><td class="py-2">S3</td><td class="py-2">Blob Storage</td><td class="py-2">Cloud Storage</td></tr>
                                    <tr><td class="py-2">Kubernetes</td><td class="py-2">EKS</td><td class="py-2">AKS</td><td class="py-2">GKE</td></tr>
                                </tbody>
                            </table>
                        </div>
                        
                        <h3 class="text-lg font-bold text-white mb-4 border-b border-slate-800 pb-2">Industry Matrix</h3>
                        <div class="grid grid-cols-2 gap-3 text-xs">
                            <div class="bg-slate-950 border border-slate-800 p-3 rounded-lg"><span class="text-slate-500 block mb-1">Startups & SaaS</span> <span class="text-emerald-400 font-bold">AWS</span> <span class="text-slate-600 text-[10px]">/ GCP</span></div>
                            <div class="bg-slate-950 border border-slate-800 p-3 rounded-lg"><span class="text-slate-500 block mb-1">Fortune 500</span> <span class="text-sky-400 font-bold">Azure</span> <span class="text-slate-600 text-[10px]">/ AWS</span></div>
                            <div class="bg-slate-950 border border-slate-800 p-3 rounded-lg"><span class="text-slate-500 block mb-1">Healthcare / Gov</span> <span class="text-emerald-400 font-bold">AWS</span> <span class="text-slate-600 text-[10px]">/ Azure</span></div>
                            <div class="bg-slate-950 border border-slate-800 p-3 rounded-lg"><span class="text-slate-500 block mb-1">Retail</span> <span class="text-emerald-400 font-bold">AWS</span> <span class="text-slate-600 text-[10px]">/ GCP</span></div>
                        </div>
                    </div>
                </div>
            </div>
"""

with open('index.html', 'r') as f:
    content = f.read()

import re

# Find the start and end of tab-career
start_marker = '<div id="tab-career"'
end_marker = '<!-- TAB: DRIFT SANDBOX -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + html + "            " + content[end_idx:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Success")
else:
    print("Could not find markers")
