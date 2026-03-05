# 🏛️ Project Coeus: Real-Time Web-Searching Agent

**Coeus** is a full-stack AI research assistant that bridges the gap between Large Language Models and the live internet. By combining a FastAPI backend with a Vite-powered React frontend, it enables users to ask complex questions and receive up-to-the-minute answers with verified source citations.

## 🚀 Key Features
* **Live Web Grounding:** Leverages Gemini's Google Search integration to bypass static knowledge cutoffs.
* **Source Transparency:** Extracts and displays specific URLs used to generate each response.
* **Modern Frontend:** Built with **Vite, TypeScript, and React** for a fast, type-safe user experience.
* **Modular Backend:** Clean separation between AI logic (`agent.py`) and API service (`main.py`).

## 🛠️ Tech Stack
* **Frontend:** React 19, Vite, TypeScript, Axios.
* **Backend:** Python 3.12+, FastAPI, Uvicorn, `google-genai`.
* **Security:** Environment variable management via `python-dotenv`.

## 📂 Project Structure
```text
AI-AGENT/
├── backend/
│   ├── venv/             # Python virtual environment
│   ├── .env              # API Key storage (Protected)
│   ├── agent.py          # Gemini AI agent & Tool config
│   └── main.py           # FastAPI routes & CORS logic
├── frontend/
│   ├── src/              # React components (App.tsx, main.tsx)
│   ├── index.html        # Entry point
│   ├── vite.config.ts    # Vite configuration
│   └── package.json      # Node dependencies
├── README.md             # Project documentation
└── .gitignore            # Git exclusion rules
