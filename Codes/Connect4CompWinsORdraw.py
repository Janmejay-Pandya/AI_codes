"""Implement Connect Four Game using min-max algorithm such
that in every play either computer wins or it is a draw. """

import numpy as np
import math
import random

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER = 0  # Human
AI = 1      # Computer
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2
WINDOW_LENGTH = 4
DEPTH = 4  # Depth limit for minimax

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Horizontal, vertical, diagonal checks
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if all([board[r][c+i] == piece for i in range(4)]):
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all([board[r+i][c] == piece for i in range(4)]):
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all([board[r+i][c+i] == piece for i in range(4)]):
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all([board[r-i][c+i] == piece for i in range(4)]):
                return True

    return False

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0
    center = list(board[:, COLUMN_COUNT//2])
    score += center.count(piece) * 3

    # Horizontal score
    for r in range(ROW_COUNT):
        row_array = list(board[r, :])
        for c in range(COLUMN_COUNT - 3):
            score += evaluate_window(row_array[c:c+4], piece)

    # Vertical score
    for c in range(COLUMN_COUNT):
        col_array = list(board[:, c])
        for r in range(ROW_COUNT - 3):
            score += evaluate_window(col_array[r:r+4], piece)

    # Positive diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # Negative diagonals
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score

def get_valid_locations(board):
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    terminal = is_terminal_node(board)

    if depth == 0 or terminal:
        if terminal:
            if winning_move(board, AI_PIECE):
                return (None, 1e9)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -1e9)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp = board.copy()
            drop_piece(temp, row, col, AI_PIECE)
            new_score = minimax(temp, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp = board.copy()
            drop_piece(temp, row, col, PLAYER_PIECE)
            new_score = minimax(temp, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

# === MAIN GAME LOOP ===

board = create_board()
game_over = False
print_board(board)

turn = random.randint(PLAYER, AI)

while not game_over:
    if turn == PLAYER:
        col = int(input("Enter column (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_PIECE)
            if winning_move(board, PLAYER_PIECE):
                print_board(board)
                print("You win!")
                game_over = True
        else:
            print("Invalid move. Try again.")
    else:
        col, _ = minimax(board, DEPTH, -math.inf, math.inf, True)
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)
            print(f"Computer chooses column {col}")
            if winning_move(board, AI_PIECE):
                print_board(board)
                print("Computer wins!")
                game_over = True

    print_board(board)

    if not game_over and len(get_valid_locations(board)) == 0:
        print("It's a draw!")
        game_over = True

    turn = (turn + 1) % 2
