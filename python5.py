def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) - 1:
                row_str += " | "
        
        print(row_str)
        if i != len(board) - 1:
            print("-" * 12)  # Fixed: added proper string multiplication


def get_move(turn, board):
    while True:
        row = int(input("Row: "))
        col = int(input("Col: "))

        if row < 1 or row > len(board):
            print("Invalid row, try again.")
        elif col < 1 or col > len(board[0]):  # Fixed: changed [row-1] to board[0]
            print("Invalid col, try again.")
        elif board[row - 1][col - 1] != " ":
            print("Already taken, try again")
        else:
            break
    board[row - 1][col - 1] = turn       
 
def check_win(board, turn):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]  # Fixed: removed extra bracket
    ]
    
    for line in lines:  # Fixed: added proper indentation
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn: 
                win = False
                break
        if win:  # Fixed: added return statement
            return True
    return False  # Fixed: added return False if no win

board = [
    ["X", " ", " "],
    [" ", "O", " "],
    [" ", " ", "X"],
]

turn = "X"
turn_number = 0
print_board(board)

while turn_number < 9:
    print()
    print("It is the", turn, "players turn. Please select your move.")
    if turn == "O":
       #computer_move()
       pass
    else:
        get_move(turn, board)
    
    print_board(board)
    winner = check_win(board, turn)
    # Fixed: Added win condition check
    if winner:
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_number += 1

if turn_number == 9:
    print("Tied game.")
else:  # Fixed: Only show tied game if no break occurred
    print("The winner was", turn) 