def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn")
        move = get_move()
        row, col = divmod(move - 1, 3)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. That spot is already taken.")
            continue

        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    play_game()
