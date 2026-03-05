import { Link } from "react-router-dom";
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul className="nav-list">
        <li>
          <Link
            style={{ textDecoration: "none" }}
            className="nav-link"
            to="/web-search"
          >
            Web Search
          </Link>
        </li>
        <li>
          <Link
            style={{ textDecoration: "none" }}
            className="nav-link"
            to="/file-search"
          >
            File Search
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
