import React from "react";
import { Link } from "react-router-dom";
import "./Home.css";
import TTT from '../assets/tic-tac-toe.png';
import chess from "../assets/chess.png";
import battleShip from "../assets/battle-ship.png";

function Home() {
  const games = [
    { id: 1, name: "Tic Tac Toe", path: "/tic-tac-toe", imgSrc: TTT },
    { id: 2, name: "Chess", path: "/chess", imgSrc: chess},
    { id: 3, name: "Battle Ship", path: "/battle-ship", imgSrc: battleShip },
    // Add more games hereg
  ];

  return (
    <div className="home-container">
      <h1 className="home-title">Game Hub</h1>
      <div className="game-list">
        {games.map((game) => (
          <Link key={game.id} to={game.path} className="game-item">
            <div className="game-name">{game.name}</div>
            <img src={game.imgSrc} alt={game.name} className="game-image" />
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Home;
