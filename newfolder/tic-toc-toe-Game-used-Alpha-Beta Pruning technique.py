import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_draw():
    return " " not in board

def minimax_ab(is_max, alpha, beta):

    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax_ab(False, alpha, beta)
                board[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break   

        return best

    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax_ab(True, alpha, beta)
                board[i] = " "
                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break  

        return best

def best_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax_ab(False, -math.inf, math.inf)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

# Game loop
while True:
    print_board()

    pos = int(input("Enter position (0-8): "))
    board[pos] = "X"

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    comp = best_move()
    board[comp] = "O"

    if check_winner("O"):
        print_board()
        print("Computer Wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break