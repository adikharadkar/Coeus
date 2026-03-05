import "./App.css";
import axios from "axios";
import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState("");
  const handleSubmit = async (e: React.MouseEvent) => {
    e.preventDefault();
    try {
      setResult("");
      setIsLoading(true);
      const response = await axios.post("http://localhost:8000/ask", {
        text: query,
      });
      setResult(response.data.answer);
      setQuery("");
    } catch (e) {
      console.log(e);
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <>
      <form
        style={{
          display: "flex",
          gap: "1rem",
          textAlign: "left",
          justifyContent: "center",
          flexDirection: "column",
        }}
      >
        <label htmlFor="query">User Query</label>
        <section
          style={{
            display: "flex",
            alignItems: "center",
            gap: "0.5rem",
          }}
        >
          <input
            type="text"
            name="query"
            id="query"
            placeholder="Enter your query here..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            style={{
              width: "65vw",
              height: "2rem",
              outline: "none",
              border: "2px solid darkslateblue",
              borderRadius: "5px",
            }}
          />
          <button
            style={{ backgroundColor: "darkslateblue", color: "white" }}
            onClick={handleSubmit}
            disabled={isLoading}
          >
            Submit
          </button>
        </section>
      </form>
      {(isLoading || result) && (
        <div
          style={{
            width: "70vw",
            textWrap: "wrap",
            borderRadius: "5px",
            boxShadow: "0 2px 2px 2px #eee",
            marginTop: "2rem",
            padding: "2rem",
          }}
        >
          {isLoading ? "Seat tight! Retriving your answer..." : result}
        </div>
      )}
    </>
  );
}

export default App;
