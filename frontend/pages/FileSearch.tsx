import axios from "axios";
import { useState } from "react";

import "./FileSearch.css";

function FileSearch() {
  const [fileId, setFileId] = useState<string | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [query, setQuery] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [chatHistory, setChatHistory] = useState<{ q: string; a: string }[]>(
    [],
  );

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsUploading(true);
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://localhost:8000/upload", formData);
    setFileId(res.data.file_id);
    setIsUploading(false);
  };

  const handleChat = async () => {
    if (!fileId || !query) return;

    try {
      // ✅ Change: Send a simple JSON object, not FormData
      setIsLoading(true);
      const payload = {
        file_id: fileId,
        text: query,
      };

      const res = await axios.post("http://localhost:8000/ask-doc", payload);

      setChatHistory([...chatHistory, { q: query, a: res.data.answer }]);
      setQuery("");
    } catch (error) {
      console.error("Error asking agent:", error);
      alert("Failed to get an answer from the document.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <h2>Step 1: Upload Document</h2>
      <input
        type="file"
        onChange={handleFileUpload}
        disabled={isUploading}
        className="file-input"
      />
      {isUploading && <p>Processing document... 🔄</p>}
      {fileId && <p>✅ Document ready for questions!</p>}

      <hr />

      <h2>Step 2: Ask Anything</h2>
      <div
        style={{
          display: "flex",
          gap: "0.5rem",
          alignItems: "center",
          justifyContent: "center",
          width: "100%",
        }}
      >
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g., What are the main risks mentioned?"
          className="query-input"
          disabled={!fileId}
          style={{ cursor: fileId ? "text" : "not-allowed", width: "70%" }}
        />
        <button onClick={handleChat} disabled={!fileId} className="ask-button">
          Ask Agent
        </button>
      </div>

      {(chatHistory.length > 0 || isLoading) && (
        <div className="chat">
          {isLoading && <p>Agent is thinking... 🤔</p>}
          {chatHistory.map((chat, i) => (
            <div key={i} className="chat-history">
              <strong>You:</strong> {chat.q} <br />
              <strong>Agent:</strong> {chat.a}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default FileSearch;
