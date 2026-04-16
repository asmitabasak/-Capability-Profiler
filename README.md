# -Capability-Profiler
CareerLaunch AI is an intelligent, agentic placement orchestration platform that automates the gap analysis between student competencies and market demand. By utilizing Agentic RAG, the system provides data-driven career coaching and predictive readiness scoring at scale.
🛠️ Tech Stack
Intelligence: Gemini 1.5 Flash (via LangChain)
API: FastAPI (Asynchronous Microservices)
Vector Store: ChromaDB (Semantic Retrieval)
Frontend: React + Vite
Infrastructure: Modular Service-Layer Design
🏗️ System Architecture
The application follows a service-layer pattern to ensure clean separation of concerns and scalability.
Ingestion Layer: Parses unstructured resumes/JDs.
Vector Store: Maps capabilities into a high-dimensional vector space.
Agentic Logic: Synthesizes retrieved market data with student profiles.
Presentation: React-based dashboard for interactive visualization.
🚀 Getting Started
Prerequisites
Python 3.10+
Node.js 18+
Gemini API Key
  # Clone the repo
Key Features
Competency Mapping: Automatically identifies "latent skills" within non-traditional student projects.
Predictive Readiness: Quantifies a student's proximity to specific job roles based on current market trends.
Bridge Program Generation: Dynamically creates 12-week study plans tailored to close specific skill gaps.
📈 Roadmap
[ ] Implement live coding sandbox for real-time technical validation.
[ ] Add visualization dashboard for placement officials to track batch readiness.
[ ] Expand vector store to include global job market data (LinkedIn/Glassdoor scraping).
📜 License
Distributed under the MIT License. See LICENSE for more information.
Pro-Tips for your GitHub:
The "Repository Image": When you upload your project to GitHub, go to Settings and add a Social Preview image. This is the thumbnail people see when you share your link.
The "Live Demo" Link: If you deploy this on Render or Vercel, put the link at the very top of the README. Recruiters love clicking a link that works.
The "Development Log": If you want to show you are serious, add a CHANGELOG.md file to your repo. It shows you know how to track versioning and project growth.
git clone https://github.com/yourusername/career-launch-ai.git

# Setup Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Setup Frontend
cd ../frontend
npm install
npm run dev
