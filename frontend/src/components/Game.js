import React, { useState, useEffect } from "react";
import Board from "./Board";
import "./Game.css";
import axios from "axios";

function Game() {
  const [game, setGame] = useState(null);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");
  const [title, setTitle] = useState("Tic Tac Toe");
  const [mode, setMode] = useState('PvP'); // Default mode is PvP

  useEffect(() => {
    startNewGame(mode);
  }, [mode]);

  useEffect(() => {
    document.title = title;
  }, [title]);

  const startNewGame = (mode) => {
    setLoading(true); // Show loading spinner
    let endpoint = '/tic-tac-toe';
    if (mode === 'Random') {
      endpoint = '/tic-tac-toe/easy';
    } else if (mode === 'Hard') {
      endpoint = '/tic-tac-toe/hard';
    }
    axios
      .post(`http://localhost:5000${endpoint}`)
      .then((response) => {
        setGame(response.data);
        setMessage("");
        setTitle("Tic Tac Toe");
        setLoading(false); // Data is ready, hide loading indicator
      })
      .catch((error) => {
        console.error("Error starting new game:", error);
        setLoading(false); // Hide loading indicator even on error
      });
  };

  const makeMove = (index) => {
    if (game.board[index] !== " " || game.status !== "ongoing") {
      return;
    }

    axios
      .post(`http://localhost:5000/tic-tac-toe/${game.id}/move`, {
        move: index,
      })
      .then((response) => {
        setGame(response.data);
        if (response.data.status === "finished") {
          if (response.data.winner) {
            setMessage(`Player ${response.data.winner} wins!`);
            setTitle(`Player ${response.data.winner} wins!`);
          } else {
            setMessage("It's a tie!");
            setTitle("It's a tie!");
          }
        }
      })
      .catch((error) => {
        console.error("Error making move:", error);
      });
  };

  const handleModeChange = (newMode) => {
    setMode(newMode);
  };

  if (loading) {
    return (
      <div className="loading-spinner-container">
        <div className="loading-spinner"></div>
      </div>
    );
  }

  if (!game) {
    return <div>Loading...</div>;
  }

  return (
    <div className="game-container">
      <h1 className="title">
        {message || <>Tic Tac Toe <span style={{ color: 'aqua' }}>{mode}</span></>}
      </h1>
      <Board board={game.board} onClick={makeMove} />
      <div>
        <button onClick={() => startNewGame(mode)}>Start New Game ({mode})</button>
      </div>
      <div style={{ marginTop: '10px' }}>
        <button style={{ marginRight: '5px' }} onClick={() => handleModeChange('Random')}>Random</button>
        <button style={{ marginRight: '5px' }} onClick={() => handleModeChange('Hard')}>Hard</button>
        <button onClick={() => handleModeChange('PvP')}>PvP</button>
      </div>
    </div>
  );
}

export default Game;
