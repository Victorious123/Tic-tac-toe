from importlib.machinery import WindowsRegistryFinder
import random
from telnetlib import PRAGMA_HEARTBEAT

# gamevariables
winner = None
player = "X"
gameRunning = True
count = 0
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# prints the game board


def printBoard(board):
    print("\n" + board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "\n")


# Input
def Input(board):
    global count
    freespot = False
    while (not freespot):

        if player == "X":
            userInput = int(input("insert number 1-9: "))
        else:
            userInput = random.randint(1, 9)

        if userInput >= 1 and userInput <= 9 and board[userInput-1] != "X" and board[userInput-1] != "O":
            board[userInput-1] = player
            freespot = True
            count += 1
        else:
            if player == "X":
                print("This spot is already taken")


# checks for the winner (whether win or tie)
def seeHorizontle(win):
    global winner
    if win[0] == win[1] == win[2]:
        winner = win[0]
        return True
    elif win[3] == win[4] == win[5]:
        winner = win[3]
        return True
    elif win[6] == win[7] == win[8]:
        winner = win[6]
        return True


def seeVertical(win):
    global winner
    if win[0] == win[3] == win[6]:
        winner = win[3]
        return True
    elif win[2] == win[5] == win[8]:
        winner = win[2]
        return True
    elif win[1] == win[4] == win[7]:
        winner = win[1]
        return True


def seeDiagonal(win):
    global winner
    if win[0] == win[4] == win[8]:
        winner = win[0]
        return True
    elif win[2] == win[4] == win[6]:
        winner = win[2]
        return True


def checkforWin():
    global gameRunning
    if seeDiagonal(board) or seeHorizontle(board) or seeVertical(board):
        print("---The winner is " + winner + "!!---")
        exit()


def checkForTie():
    if count == 9:
        print("---You've got a tie!!---")
        exit()


# changing the player
def changePlayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# game loops
while (gameRunning):
    printBoard(board)
    checkforWin()
    checkForTie()
    print("current player: " + player)
    Input(board)
    changePlayer()
