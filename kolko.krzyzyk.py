def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Gracz {current_player}, wybierz wiersz (0-2): "))
            col = int(input(f"Gracz {current_player}, wybierz kolumnę (0-2): "))
        except ValueError:
            print("Błędne dane. Spróbuj ponownie.")
            continue

        if row not in range(3) or col not in range(3):
            print("Poza zakresem planszy spróbuj ponownie")
            continue
        if board[row][col] != " ":
            print("No to już jest zajęte")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Gracz {current_player} wygrywa!")
            break
        if is_full(board):
            print_board(board)
            print("Remis! niestety jest remisik lub stety")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
