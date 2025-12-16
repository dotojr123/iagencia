# Jules AI Agency 🦅

**Version:** 1.0.0
**Status:** Initial Release (Dec 2025)

Jules is an autonomous AI agency designed to handle complex tasks through a network of specialized agents. This repository features a hybrid architecture separating the AI Agentic Core (Python) from the User Interface (Next.js).

## 🏗 Architecture

### 1. Backend (AI Core)
*   **Location:** `julius-ai-agency/backend-ai`
*   **Tech Stack:** Python 3.11+, CrewAI 1.7+, FastAPI, LangGraph.
*   **Function:** Handles all intelligence, agent orchestration, and task execution.
*   **Deployment:** Ready for Railway, Render, or any VPS.

### 2. Frontend (Dashboard)
*   **Location:** `julius-ai-agency/frontend-dashboard`
*   **Tech Stack:** Next.js 14, React 18, TailwindCSS.
*   **Function:** User interface for dispatching tasks and viewing reports.
*   **Deployment:** Optimized for Vercel.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Node.js 18+
*   OpenAI / Gemini API Keys

### 1. Setup Backend
```bash
cd julius-ai-agency/backend-ai

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure Environment
cp .env.example .env
# Edit .env and add your API keys (OPENAI_API_KEY, GEMINI_API_KEY)

# Run Server
python src/main.py
# API will be running at http://localhost:8000
```

### 2. Setup Frontend
```bash
cd julius-ai-agency/frontend-dashboard

# Install dependencies
npm install

# Configure Environment
cp .env.example .env.local
# Ensure NEXT_PUBLIC_API_URL is set to http://localhost:8000

# Run Development Server
npm run dev
# Dashboard available at http://localhost:3000
```

---

## 📚 Documentation
*   [Architecture Overview](docs/ARCHITECTURE.md)
*   [API Documentation](docs/API.md)
*   [Deployment Guide](docs/DEPLOYMENT.md)

## 🤝 Contributing
1.  Fork the repo
2.  Create your feature branch (`git checkout -b feature/amazing-feature`)
3.  Commit your changes (`git commit -m 'Add some amazing feature'`)
4.  Push to the branch (`git push origin feature/amazing-feature`)
5.  Open a Pull Request
