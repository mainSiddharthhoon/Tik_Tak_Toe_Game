import sys

rows = 3
cols = 3
global_count = 0
matrix_field = [[None for _ in range(cols)] for _ in range(rows)]

def x(Rows, Cols):
    global global_count
    global matrix_field

    if Rows == 0 and Cols == 0:
        print("Programme Exited Successfully!")
        sys.exit()

    if Rows < 1 or Rows > 3 or Cols < 1 or Cols > 3:
        print("Please enter valid rows and cols(in range 1 to 3)!")
        return 6

    # Place move
    if matrix_field[Rows-1][Cols-1] is None:
        matrix_field[Rows-1][Cols-1] = 1
        global_count += 1
    else:
        print("This place is already taken!")
        print("Please enter any valid location coordinates in board.")
        return 5

    # Check rows
    for i in range(rows):
        count1 = 0
        for j in range(cols):
            if matrix_field[i][j] == 1:
                count1 += 1
        if count1 == 3:
            print("Player1 with X has won the match! Whoo ray! X won!")
            sys.exit()

    # Check columns
    for j in range(cols):
        count2 = 0
        for i in range(rows):
            if matrix_field[i][j] == 1:
                count2 += 1
        if count2 == 3:
            print("Player1 with X has won the match! Whoo ray! X won!")
            sys.exit()

    # Check diagonals
    count3 = 0
    count4 = 0

    if matrix_field[0][0] == 1:
        count3 += 1
    if matrix_field[1][1] == 1:
        count3 += 1
    if matrix_field[2][2] == 1:
        count3 += 1

    if matrix_field[0][2] == 1:
        count4 += 1
    if matrix_field[1][1] == 1:
        count4 += 1
    if matrix_field[2][0] == 1:
        count4 += 1

    if count3 == 3 or count4 == 3:
        print("Player1 with X has won the match! Whoo ray! X won!")
        sys.exit()
    if global_count == 9:
        print("Match drawn!")
        sys.exit()
    # Print board
    print("Current board:")
    for i in range(rows):
        for j in range(cols):
            cell = matrix_field[i][j]
            if cell is None:
                print(" . ", end="")
            elif cell == 1:
                print(" X ", end="")
            else:
                print(" O ", end="")
        print()


def o(Rows, Cols):
    global global_count
    global matrix_field

    if Rows == 0 and Cols == 0:
        print("Programme exited successfully!")
        sys.exit()

    if Rows < 1 or Rows > 3 or Cols < 1 or Cols > 3:
        print("Please enter valid rows and cols(in range 1 to 3)!")
        return 4

    # Place move
    if matrix_field[Rows-1][Cols-1] is None:
        matrix_field[Rows-1][Cols-1] = 0
        global_count += 1
    else:
        print("This place is already taken!")
        print("Please enter any valid location coordinates in board.")
        return 3

    # Check rows
    for i in range(rows):
        count1 = 0
        for j in range(cols):
            if matrix_field[i][j] == 0:
                count1 += 1
        if count1 == 3:
            print("Player2 with 0 has won the match! Whoo ray! 0 won!")
            sys.exit()

    # Check columns
    for j in range(cols):
        count2 = 0
        for i in range(rows):
            if matrix_field[i][j] == 0:
                count2 += 1
        if count2 == 3:
            print("Player2 with 0 has won the match! Whoo ray! 0 won!")
            sys.exit()

    # Check diagonals
    count3 = 0
    count4 = 0

    if matrix_field[0][0] == 0:
        count3 += 1
    if matrix_field[1][1] == 0:
        count3 += 1
    if matrix_field[2][2] == 0:
        count3 += 1

    if matrix_field[0][2] == 0:
        count4 += 1
    if matrix_field[1][1] == 0:
        count4 += 1
    if matrix_field[2][0] == 0:
        count4 += 1

    if count3 == 3 or count4 == 3:
        print("Player2 with 0 has won the match! Whoo ray! 0 won!")
        sys.exit()
    if global_count == 9:
        print("Match drawn!")
        sys.exit()
    # Print board
    print("Current board:")
    for i in range(rows):
        for j in range(cols):
            cell = matrix_field[i][j]
            if cell is None:
                print(" . ", end="")
            elif cell == 1:
                print(" X ", end="")
            else:
                print(" O ", end="")
        print()


# Game intro
print("Hello User! Welcome to tic-tac-toe game CLI version.")
print("Here there will be two players: player1 and player2.")
print("Player 1 will get X as their operator.")
print("Player 2 will get 0 as their operator.")
print("Player 1 will get the first chance.")
print("Its a beta version so some less functionalities are there")
print("We are really sorry for that.")
print("Here according to your turn you will have to write the rows and cols coordinates")
print("Please enter valid rows and cols (in range 1-3).")
print("Ok, let's start the game!\n")

count = 1

while True:
    if count % 2 == 0:
        Rows2 = int(input("Hello player 2 please enter rows: "))
        Cols2 = int(input("Hello player 2 please enter cols: "))
        variable2 = o(Rows2, Cols2)
        while variable2 == 4 or variable2 == 3:
            Rows2 = int(input("Hello player 2 please enter rows: "))
            Cols2 = int(input("Hello player 2 please enter cols: "))
            variable2 = o(Rows2, Cols2)
        count += 1
    else:
        Rows1 = int(input("Hello player 1 please enter rows: "))
        Cols1 = int(input("Hello player 1 please enter cols: "))
        variable1 = x(Rows1, Cols1)
        while variable1 == 6 or variable1 == 5:
            Rows1 = int(input("Hello player 1 please enter rows: "))
            Cols1 = int(input("Hello player 1 please enter cols: "))
            variable1 = x(Rows1, Cols1)
        count += 1
 
