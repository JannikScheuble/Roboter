# !/usr/bin/env python3
import robot_control as ctrl
from robot_ai_module import *
from board import *
from time import sleep
import ev3dev.ev3 as ev3
import copy as copy

def getOpponentInput(board):
    row = None
    col = None

    while True:
        while True:
            # Try catch in case the user inputs a non-numeric value
            try:
                row = int(input("Which row did the opponent place its block at: "))
            except:
                row = None

            if row == None or row < 0 or row > 2:
                print("Invalid row. Please make sure to enter a number from 0 to 2 (inclusive).")
            else:
                break

        while True:
            # Try catch in case the user inputs a non-numeric value
            try:
                col = int(input("Which column did the opponent place its block at: "))
            except:
                col = None

            if col == None or col < 0 or col > 2:
                print("Invalid column. Please make sure to enter a number from 0 to 2 (inclusive).")
            else:
                break

        if board.GetField(row, col) != 0:
            print("The field you tried to select is already occupied. Please check your input.")
        else:
            sureYN = None
            while True:
                print("Input was: row: " + str(row) + ", col: " + str(col))
                print("Does the board now look like this?")
                newBoard = copy.copy(board)
                newBoard.SetField(row, col, 2)
                newBoard.PrintBoard()
                sureYN = input("Are you sure that your input is correct?" + "\nEnter 'Y' for yes, 'N' for no: ")
                if sureYN == "N" or sureYN == "Y":
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'!")

            if sureYN == "Y":
                break

    return row, col

def makeOpponentMove(board):
    opponentInputRow, opponentInputCol = getOpponentInput(board)
    board.SetField(opponentInputRow, opponentInputCol, 2)

def makeAIMove(ai, board):
    nextMove = ai.getNextMove(board, 0)

    nextMoveForControl = 3 * nextMove[0] + nextMove[1] + 1

    ctrl.pickingupblocks()  # Motor gets its block
    sleep(2)
    ctrl.navigatesquare(nextMoveForControl)

    board.SetField(nextMove[0], nextMove[1], 1)

 # Main Code that will be executed
if __name__ == '__main__':
    ai = AI("ai_first_moves.ai")
    board = Board()

    print("Start")
    currentPlayer = None

    while not (currentPlayer == 0 or currentPlayer == 1):
        currentPlayer = int(input("Who is starting (0: we are starting, 1: opponent is starting): "))
        if not (currentPlayer == 0 or currentPlayer == 1):
            print("Invalid input. Please make sure to input valid values. (See input prompt)")

    while True:
        if currentPlayer == 0:
            makeAIMove(ai, board)
        else:
            makeOpponentMove(board)

        print("Current board state:")
        board.PrintBoard()

        winState = board.CheckWinState()
        if winState == 2:
            print("Draw!")
            ev3.Sound.speak("It's a draw!").wait()
            break
        elif winState == 0:
            print("We won!")
            ev3.Sound.speak("We won!").wait()
            break
        elif winState == 1:
            print("They won. IMPOSSIBLE...")
            ev3.Sound.speak("They won. IMPOSSIBLE...").wait()
            break

        # Next players turn
        currentPlayer = (currentPlayer + 1) % 2