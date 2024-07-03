import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "./components/Home";
import Game from "./components/Game";
import flamesLogo from "../src/assets/flames-logo.png";
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <Link to="/">
          <img src={flamesLogo} alt="Logo" className="logo" />{" "}
        </Link>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/tic-tac-toe" element={<Game />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
