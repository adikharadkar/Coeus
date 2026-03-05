# 🏛️ Project Coeus: Hybrid AI Research Agent

**Coeus** is a full-stack AI research assistant that bridges the gap between Large Language Models, the live internet, and your personal data. By combining a FastAPI backend with a Vite-powered React frontend, it enables users to switch between real-time web research and deep-dive document analysis.

## 🚀 Key Features

- **Hybrid Grounding:**
  - **Web Search:** Uses Google Search to bypass knowledge cutoffs for current events.
  - **Document RAG:** Securely processes uploaded PDFs/documents to provide answers grounded strictly in your files.
- **Source Transparency:** Displays specific URLs for web searches and clear file references for document analysis.
- **Modern Frontend:** Built with **Vite, TypeScript, and React** for a fast, responsive user experience.
- **Efficient Backend:** Uses an asynchronous FastAPI architecture to handle both web-scraping and file-indexing without blocking.

## 🛠️ Tech Stack

- **Frontend:** React 19, Vite, TypeScript, Axios.
- **Backend:** Python 3.12+, FastAPI, Uvicorn, `google-genai`.
- **AI Core:** Gemini 2.5 Flash (via Google GenAI SDK).
- **Environment:** `python-dotenv`.

## 📂 Project Structure

```text
AI-AGENT/
├── backend/
│   ├── agent.py          # Hybrid Agent (Search + RAG logic)
│   ├── main.py           # FastAPI routes (Uploads, Search, Doc Query)
│   └── .env              # API Keys (Protected)
├── frontend/
│   └── src/
│       └── FileSearch.tsx # Document upload & RAG interface
└── README.md             # Documentation
```

## ⚡ Setup & Installation

### 1. Backend Setup

Navigate to the `backend` directory:

```bash
cd backend
```

**i. Install Dependencies**

```bash
pip install fastapi uvicorn google-genai python-dotenv
```

**ii. Configure Environment Variables**

Ensure your `.env` file contains your API key:

```plaintext
GEMINI_API_KEY=your_actual_api_key_here
```

**iii. Run the Server**

```bash
uvicorn main:app --reload
```

---

### 2. Frontend Setup

Open a new terminal and navigate to the `frontend` directory:

```bash
cd frontend
```

**i. Install Packages**

```bash
npm install
```

**ii. Run Development Server**

```bash
npm run dev
```

---

## 🧠 How the RAG Feature Works

1. **Upload:** Your PDF is sent to the `/upload` endpoint, where it is saved temporarily and uploaded to Gemini's File API.
2. **Indexing:** The agent waits for the file state to transition to `ACTIVE` before allowing queries.
3. **Hybrid Routing:**
   - **Web Query:** Uses a persistent chat session with the Google Search tool.
   - **Doc Query:** Uses a fresh `generate_content` call, injecting the `file_id` as context — ensuring the AI focuses only on your provided document.

## 🛡️ Security & Best Practices

| Practice | Description |
|---|---|
| **File Lifecycle** | Temporary files are automatically deleted from the server after the upload process, preventing disk clutter. |
| **Stateful Polling** | The agent uses `asyncio` to poll the Gemini File API, ensuring the server stays responsive while waiting for document indexing. |
| **CORS Control** | Strict `CORSMiddleware` configuration ensures only trusted frontends communicate with your API. |
