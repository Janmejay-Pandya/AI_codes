"""Implement Connect Four Game using min-max algorithm such
that in every play either computer loses or it is a draw. """

import numpy as np
import random

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER_PIECE = 1
AI_PIECE = 2

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == 0

def get_valid_locations(board):
    return [col for col in range(COLUMN_COUNT) if is_valid_location(board, col)]

def get_next_open_row(board, col):
    for r in range(ROW_COUNT-1, -1, -1):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))  # Flip so the bottom row prints last (like gravity)

def winning_move(board, piece):
    # Check horizontal
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT-3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Check positive diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Check negative diagonal
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT-3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False

# Start the game
board = create_board()
game_over = False
turn = 0  # 0 for player, 1 for AI

print_board(board)

while not game_over:
    if turn == 0:
        # Player Turn
        col = int(input("Player 1 Make your Selection (0-6): "))
        if 0 <= col < COLUMN_COUNT and is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_PIECE)

            if winning_move(board, PLAYER_PIECE):
                print_board(board)
                print("PLAYER 1 WINS!")
                game_over = True

            turn = 1
        else:
            print("Invalid move. Try again.")
    else:
        # Computer (bad AI) Turn
        valid_locations = get_valid_locations(board)
        lose_moves = []

        for col in valid_locations:
            temp_board = board.copy()
            row = get_next_open_row(temp_board, col)
            drop_piece(temp_board, row, col, AI_PIECE)

            if not winning_move(temp_board, AI_PIECE):
                lose_moves.append(col)

        # If all moves win, allow randomly
        if lose_moves:
            col = random.choice(lose_moves)
        else:
            col = random.choice(valid_locations)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)
            print(f"Computer chooses column {col}")

            if winning_move(board, AI_PIECE):
                print_board(board)
                print("COMPUTER WINS! (unexpected!)")
                game_over = True

            turn = 0

    print_board(board)

    # Check draw
    if not get_valid_locations(board) and not game_over:
        print("DRAW! No more moves.")
        game_over = True
