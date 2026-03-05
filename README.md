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

⚡ Setup & Installation
Follow these steps to get the project running locally.

1. Prerequisites
Node.js (v18 or higher)

Python (3.10 or higher)

Gemini API Key (Obtain one at Google AI Studio)

2. Backend Setup
Navigate to the backend directory:

Bash
cd backend
Create and Activate Virtual Environment:

Windows:

Bash
python -m venv venv
venv\Scripts\activate
Mac/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

Bash
pip install fastapi uvicorn google-genai python-dotenv
Configure Environment Variables:
Create a .env file in the backend/ folder and add your key:

Plaintext
GEMINI_API_KEY=your_actual_api_key_here
Run the Server:

Bash
uvicorn main:app --reload
3. Frontend Setup
Open a new terminal and navigate to the frontend directory:

Bash
cd frontend
Install Packages:

Bash
npm install
Run Development Server:

Bash
npm run dev
🛡️ Security & Best Practices
Environment Isolation: Sensitive credentials like the GEMINI_API_KEY are stored in a local .env file. This file is explicitly ignored by Git to prevent leaking secrets to public repositories.

CORS Middleware: The FastAPI backend implements CORSMiddleware to strictly control which frontend origins can access the API, preventing unauthorized cross-origin requests.

Asynchronous Execution: By utilizing async endpoints in FastAPI, the agent can handle I/O-bound tasks (like web searching) without blocking the server, ensuring high availability.

Dependency Locking: Python dependencies are managed within a virtual environment (venv) to ensure a consistent, reproducible execution environment across different development machines.
