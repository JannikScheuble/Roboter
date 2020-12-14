# !/usr/bin/env python3
import robot_control as ctrl
from robot_ai_module import *
from board import *
from time import sleep
import ev3dev.ev3 as ev3
import copy as copy
from robot_control import *

def getOpponentInput(board):

    while True:
        row = 0
        col = 0

    # Try catch in case the user inputs a non-numeric value
        is_invalid = False
        while not ts2.value():
            if ts1.value():
                row += 1
                ev3.Sound.speak("Row, ",row,"Selected").wait()
                sleep(0.5)
        sleep(1.0)
        print(row)
        while not ts2.value() and not is_invalid:
            if ts1.value():
                col += 1
                ev3.Sound.speak("Colum ",col, "Selected").wait()
                sleep(0.5)


        sleep(1.0)

        print(col)

        if col < 0 or col > 2:
            ev3.Sound.speak("Invalid column. Please make sure to enter a number from 0 to 2 (inclusive).")
            print("Invalid column. Please make sure to enter a number from 0 to 2 (inclusive).")
            is_invalid = True
        if row < 0 or row > 2:
            ev3.Sound.speak("Invalid row. Please make sure to enter a number from 0 to 2 (inclusive).")
            print("Invalid row. Please make sure to enter a number from 0 to 2 (inclusive).")
            is_invalid = True


        if is_invalid:
            print("Invalid")
        elif board.GetField(row, col) != 0:
           print("The field you tried to select is already occupied. Please check your input.")
        else:
            sureYN = None
            while True:
                print("Input was: row: " + str(row) + ", col: " + str(col))
                print("Does the board now look like this?")
                newBoard = copy.copy(board)
                newBoard.SetField(row, col, 2)
                newBoard.PrintBoard()
                ev3.Sound.speak("Are the inputs correct").wait()
                while not (ts1.value() or ts2.value()):
                    sleep(0.1)
                    if ts1.value() == 1:
                        sureYN = "Y"
                    elif ts2.value() == 1:
                        sureYN = "N"
                    #sureYN = input("Are you sure that your input is correct?" + "\nEnter 'Y' for yes, 'N' for no: ")
                if sureYN == "N" or sureYN == "Y":
                    break
                else:
                    print("Invalid input. Please press Sensor 1 or 2!")

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
    navigatesquare(nextMoveForControl)

    board.SetField(nextMove[0], nextMove[1], 1)

 # Main Code that will be executed
if __name__ == '__main__':
    ai = AI("ai_first_moves.ai")
    board = Board()

    ev3.Sound.speak("Start the game")
    currentPlayer = None

    while not (currentPlayer == 0 or currentPlayer == 1):
        while not (ts1.value() or ts2.value()):
            sleep(0.01)

        if ts1.value() == 1:  #robot begins
            currentPlayer = 0
            ev3.Sound.speak("We Start")
        elif ts2.value() == 1: #player beginns
            ev3.Sound.speak("You start")
            currentPlayer = 1
       #currentPlayer = int(input("Who is starting (0: we are starting, 1: opponent is starting): "))
       #if not (currentPlayer == 0 or currentPlayer == 1):
           #print("Invalid input. Please make sure to input valid values. (See input prompt)")

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
        ev3.Sound.speak("Turn change")
        currentPlayer = (currentPlayer + 1) % 2
