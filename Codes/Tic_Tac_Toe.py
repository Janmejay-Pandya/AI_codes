import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

board = [[' ' for _ in range(3)] for _ in range(3)]

while True:
    print_board(board)
    x = int(input("Enter row (0-2): "))
    y = int(input("Enter col (0-2): "))
    if board[x][y] != ' ':
        print("Invalid move, try again.")
        continue
    board[x][y] = 'X'

    if check_winner(board, 'X'):
        print_board(board)
        print("You win! (Not supposed to happen 😅)")
        break
    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break

    comp_move = best_move(board)
    board[comp_move[0]][comp_move[1]] = 'O'

    if check_winner(board, 'O'):
        print_board(board)
        print("Computer wins!")
        break
    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break
