#!/usr/bin/env python3
from robot_ai_module import *
from board import *

def makeMove(board, player, fieldRow, fieldCol):
    board.SetField(fieldRow, fieldCol, player + 1)

def makeUserMove(board, player):
    row = int(input("Select your row: "))
    col = int(input("Select you column: "))

    makeMove(board, player, row, col)

    board.PrintBoard()

# The AI move is always player 0 for now!!!
def makeAIMove(ai, board):
    nextMove = ai.getNextMove(board, 0)
    makeMove(board, 0, nextMove[0], nextMove[1])
    board.PrintBoard()

def mainTest():
    # Error checking is omitted for ai testing
    ai = AI("ai_first_moves.ai")

    board = Board()
    board.PrintBoard()
    player = 1

    while True:
        if player == 1:
            makeUserMove(board, player)
        else:
            makeAIMove(ai, board)

        winState = board.CheckWinState()
        if winState != -1:
            if winState == 2:
                print("Draw!")
                break
            elif winState == 1:
                print("You won!")
                break
            else:
                print("You lost! AI won!")
                break

        # Make the other player have their move.
        player = (player + 1) % 2

mainTest()