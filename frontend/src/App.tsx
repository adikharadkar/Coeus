import { Route, Routes } from "react-router-dom";

import "./App.css";
import Navbar from "../components/Navbar";
import WebSearch from "../pages/WebSearch";
import FileSearch from "../pages/FileSearch";

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/web-search" element={<WebSearch />} />
        <Route path="/file-search" element={<FileSearch />} />
      </Routes>
    </>
  );
}

export default App;
