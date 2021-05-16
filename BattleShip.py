# Battle Ships

from sys import stdout
from random import random

# initialize Boards

enemyBoard = [[0 for x in range(10)] for y in range(10)]
for i in range(len(enemyBoard)):
    for j in range(len(enemyBoard)):
        enemyBoard[i][j] = "_"

enemyBoardInvisible = [[0 for x in range(10)] for y in range(10)]
for i in range(len(enemyBoardInvisible)):
    for j in range(len(enemyBoardInvisible)):
        enemyBoardInvisible[i][j] = "_"

playerBoard = [[0 for x in range(10)] for y in range(10)]
for i in range(len(playerBoard)):
    for j in range(len(playerBoard)):
        playerBoard[i][j] = "_"


# Function that plots random boats for
# the enemy/computer player


def randomBoat(size):

    # Initialize Ship
    direction = int(random()*2)
    posX = int(random() * (11 - size))
    posY = int(random() * (11 - size))

    if direction == 1:

        for i in range(0, size):
            if enemyBoard[posX+i][posY] != "_":
                randomBoat(size)
                return
        for i in range(0,size):
            enemyBoard[posX+i][posY] = "O"
    else:
        for i in range(0, size):
            if enemyBoard[posX][posY+i] != "_":
                randomBoat(size)
                return
        for i in range(0,size):
            enemyBoard[posX][posY+i] = "O"

# Prints board, takes a board type, and an ID,
# which is only used for the board title
def printBoard(boardType, ID):

    print("\n-------- " + ID + " Board ---------")
    print("   0  1  2  3  4  5  6  7  8  9")
    for i in range(len(boardType)):
        stdout.write(str(i) + " ")
        for j in range(len(boardType)):
            stdout.write("[" + boardType[i][j]+ "]")
        stdout.write("\n")


# Player plots boat, asks for direction, X coordinate
# and y coordinate. Checks if in range


def plotBoat(size):

    print("Boat size: " + str(size))
    direction = input("Type in right or down: ")
    posX = int(input("Type in X coordinate: "))
    posY = int(input("Type in Y coordinate: "))

    if direction == "down":

        for i in range(0, size):
            if  posY >= 11-size or posX > 9 or playerBoard[posY + i][posX] != "_":
                print("Position is either taken or out of range, please try again.")
                plotBoat(size)
                return

        for i in range(0, size):
            playerBoard[posY + i][posX] = "O"
    elif direction == "right":

        for i in range(0, size):

            if posY > 9 or posX >= 11-size or playerBoard[posY][posX + i] != "_":
                print("Position is either taken or out of range, please try again.")
                plotBoat(size)
                return

        for i in range(0, size):
            playerBoard[posY][posX + i] = "O"
    printBoard(playerBoard, "Player")

# Enemy/computer attacks player, plots randomly
# but does not attack in the same place twice

def attackPlayer():
    xAttack = int(random()*10)
    yAttack = int(random()*10)

    if playerBoard[yAttack][xAttack] != "_" and playerBoard[yAttack][xAttack] != "#":
        playerBoard[yAttack][xAttack] = "X"
    else:
        playerBoard[yAttack][xAttack] = "#"
    printBoard(enemyBoardInvisible, "Enemy")
    printBoard(playerBoard, "Player")


# Player attacks enemy, asks for X and Y coordinates, will
# not break out of while loop until a new place is hit/plot
# is in range


def attackEnemy():

    while(True):

        print("\nYour turn to attack!")
        xAttack = int(input("Type in X coordinate: "))
        yAttack = int(input("Type in Y coordinate: "))

        if xAttack < 10 and yAttack < 10:
            if enemyBoard[yAttack][xAttack] != "_" and enemyBoard[yAttack][xAttack] != "#":
                enemyBoard[yAttack][xAttack] = "X"
                enemyBoardInvisible[yAttack][xAttack] = "X"
            else:
                enemyBoard[yAttack][xAttack] = "#"
                enemyBoardInvisible[yAttack][xAttack] = "#"
            break

# Checks who wins, if there are no ships (O) left, it will
# return "(ID) wins!"

def winCheck(boardType, ID):
    for i in range(len(boardType)):
        for j in range(len(boardType)):
            if boardType[i][j] == "O":
                return
    print("\n" + ID + " wins!")
    exit(0)


# The main function; enemy plots boats first, then player
# plots boats. Player cannot see enemy's ships, only a
# board that represents hits and misses. Checks if anyone
# wins at the end of the while loop. Program ends when one
# side wins.

def main():

    randomBoat(5)
    randomBoat(4)
    randomBoat(3)
    randomBoat(3)
    randomBoat(2)

    printBoard(playerBoard, "Player")

    plotBoat(5)
    plotBoat(4)
    plotBoat(3)
    plotBoat(3)
    plotBoat(2)

    printBoard(enemyBoardInvisible, "Enemy")
    printBoard(playerBoard, "Player")

    while True:
        attackEnemy()
        attackPlayer()
        winCheck(playerBoard, "Enemy")
        winCheck(enemyBoard, "Player")

main()