from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from game import *
import random

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
        
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.String(9), nullable=False)  # Store the board as a string of length 9
    current_player = db.Column(db.String(1), nullable=False)  # 'X' or 'O'
    status = db.Column(db.String(10), nullable=False)  # 'ongoing', 'finished', etc.
    winner = db.Column(db.String(1), nullable=True)  # 'X', 'O', or None
    mode = db.Column(db.String(20), nullable=False)  # 'minimax', 'random', 'pvp'

    def to_json(self):
        return {
            "id": self.id,
            "board": list(self.board),  # Convert the string back to a list of characters
            "currentPlayer": self.current_player,
            "status": self.status,
            "winner": self.winner,
            "mode": self.mode,
        }
        
@app.route('/tic-tac-toe', methods=['POST'])
def new_game():
    board = ' ' * 9
    game = Game(board=board, current_player='X', status="ongoing", winner=None, mode='PvP')
    db.session.add(game)
    db.session.commit()
    return jsonify(game.to_json())

@app.route('/tic-tac-toe/hard', methods=['POST'])
def new_game_minimax():
    board = ' ' * 9  # Initialize an empty board
    game = Game(board=board, current_player='X', status='ongoing', winner=None, mode='Hard')
    db.session.add(game)
    db.session.commit()
    return jsonify(game.to_json())

@app.route('/tic-tac-toe/easy', methods=['POST'])
def new_game_random():
    board = ' ' * 9  # Initialize an empty board
    game = Game(board=board, current_player='X', status='ongoing', winner=None, mode='Random')
    db.session.add(game)
    db.session.commit()
    return jsonify(game.to_json())
        
@app.route('/tic-tac-toe/<int:game_id>/move', methods=['POST'])
def make_move(game_id):
    game = Game.query.get(game_id)
    if not game or game.status != 'ongoing':
        return jsonify({'error': 'Invalid game or game already finished'}), 400

    data = request.get_json()
    move = data.get('move')
    if move is not None:
        if game.board[move] != ' ':
            return jsonify({'error': 'Invalid move'}), 400

        board_list = list(game.board)
        board_list[move] = game.current_player
        game.board = ''.join(board_list)

        winner = check_for_win(game.board)
        if winner:
            game.status = 'finished'
            game.winner = winner
            db.session.commit()
            return jsonify(game.to_json())

        if check_for_tie(game.board):
            game.status = 'finished'
            game.winner = None
            db.session.commit()
            return jsonify(game.to_json())

        if game.mode == 'PvP':
            game.current_player = 'O' if game.current_player == 'X' else 'X'
        elif game.mode == 'Hard':
            # CPU move with Minimax
            if game.current_player == 'X':
                cpu_move = get_best_move(board_list, 'O', 'X')
                if cpu_move is not None:
                    board_list[cpu_move] = 'O'
                    game.board = ''.join(board_list)

                    winner = check_for_win(game.board)
                    if winner:
                        game.status = 'finished'
                        game.winner = winner
                        db.session.commit()
                        return jsonify(game.to_json())

                    if check_for_tie(game.board):
                        game.status = 'finished'
                        game.winner = None
                        db.session.commit()
                        return jsonify(game.to_json())

                    game.current_player = 'X'
        elif game.mode == 'Random':
            # CPU move with random choice
            if game.current_player == 'X':
                empty_spots = [i for i, spot in enumerate(game.board) if spot == ' ']
                if empty_spots:
                    cpu_move = random.choice(empty_spots)
                    board_list[cpu_move] = 'O'
                    game.board = ''.join(board_list)

                    winner = check_for_win(game.board)
                    if winner:
                        game.status = 'finished'
                        game.winner = winner
                        db.session.commit()
                        return jsonify(game.to_json())

                    if check_for_tie(game.board):
                        game.status = 'finished'
                        game.winner = None
                        db.session.commit()
                        return jsonify(game.to_json())

                    game.current_player = 'X'
        
        db.session.commit()
        return jsonify(game.to_json())

@app.route('/tic-tac-toe/<int:game_id>/result', methods=['GET'])
def get_result(game_id):
    game = Game.query.get(game_id)
    if game:
        winner = check_for_win(game.board)
        if winner:
            game.status = 'finished'
            game.winner = winner
            db.session.commit()
        elif check_for_tie(game.board):
            game.status = 'finished'
            game.winner = None
            db.session.commit()
        return jsonify(game.to_json())
    return jsonify({'error': 'Game not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
    