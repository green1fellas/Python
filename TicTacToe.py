from sys import stdout
running = True
turn = "X"

# Initialize board
board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]

while running:

    for i in range(len(board)):
        for j in range(len(board)):
            stdout.write("[" + board[i][j]+ "]")
        stdout.write("\n")

    # Check
    #-----------------------------------
    for i in range(len(board)):
        if (board[0][i] == board[1][i] == board[2][i] != "_"):
            print(board[0][i] + " wins!")
            exit(0)
        elif (board[i][0] == board[i][1] == board[i][2] != "_"):
            print(board[i][0] + " wins!")
            exit(0)


    if (board[0][0] == board[1][1] == board[2][2] != "_"):
        print(board[i][0] + " wins!")
        exit(0)
    if(board[0][2] == board[1][1] == board[2][0] != "_"):
        print(board[i][0] + " wins!")
        exit(0)

    #-------------------------------------

    print("It is " + turn + "'s turn")
    x = int(input("Type x coordinate: "))
    y = int(input("Type y coordinate: "))

    if board[y][x] == "_":
        board[y][x] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    else:
        print("Space taken, try again.")

