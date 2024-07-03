# Checks for a win
def check_for_win(board):
    winning_combinations = [
        # Rows
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        # Columns
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        # Diagonals
        [0, 4, 8],
        [2, 4, 6],
    ]

    for combination in winning_combinations:
        a, b, c = combination
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    
    return None

# Checks for a tie
def check_for_tie(board):
    return ' ' not in board

# Recursive function that simulates all possible moves to determine the best move for the CPU.
def minimax(board, depth, is_maximizing, player, opponent):
    winner = check_for_win(board)
    if winner == player:
        return 1
    elif winner == opponent:
        return -1
    elif check_for_tie(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = player
                score = minimax(board, depth + 1, False, player, opponent)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = opponent
                score = minimax(board, depth + 1, True, player, opponent)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

#  Uses the Minimax algorithm to find the optimal move for the CPU.
def get_best_move(board, player, opponent):
    best_score = -float('inf')
    best_move = None
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = player
            score = minimax(board, 0, False, player, opponent)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move