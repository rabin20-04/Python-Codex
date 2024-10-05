def print_board(X_state, Z_state):
    zero = "X" if X_state[0] else ("0" if Z_state[0] else 0)
    one = "X" if X_state[1] else ("O" if Z_state[1] else 1)
    two = "X" if X_state[2] else ("O" if Z_state[2] else 2)
    three = "X" if X_state[3] else ("O" if Z_state[3] else 3)
    four = "X" if X_state[4] else ("O" if Z_state[4] else 4)
    five = "X" if X_state[5] else ("O" if Z_state[5] else 5)
    six = "X" if X_state[6] else ("O" if Z_state[6] else 6)
    seven = "X" if X_state[7] else ("O" if Z_state[7] else 7)
    eight = "X" if X_state[8] else ("O" if Z_state[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")


def checkWin(X_state, Z_state):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for win in wins:
        if sum(X_state[win[0]], X_state[win[1]], X_state[win[2]]) == 3:
            print("X Won the match")
            return 1
        if sum(Z_state[win[0]], Z_state[win[1]], Z_state[win[2]]) == 3:
            print("O Won the match")
            return 0
    return -1


if __name__ == "__main__":
    X_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Z_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(" ************* Welcome to TIC TAC TOE *************\n")
    turn = 1  # 1 for X and 0 for O
    while True:
        if turn == 1:
            print_board(X_state, Z_state)

            print("X's chance ")
            value = int(input("Enter a value: "))
            X_state[value] = 1
        else:
            print("O's chance ")
            value = int(input("Enter a value: "))
            Z_state[value] = 1
        cwin = checkWin(X_state, Z_state)
        if cwin != -1:
            print("Match over")
            break

        turn = 1 - turn
