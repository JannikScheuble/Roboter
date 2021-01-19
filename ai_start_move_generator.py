from board import *
from robot_ai_module import *
import copy as copy

maxDepth = 3

# Generate starting moves to depth maxDepth, since calculating the first few moves is very expensive. Then save them
# to a file so we can use them on the robot.

def writeMoveToFile(file, depth, board, nextMove):
    file.write(str(board.SerializeBoard()) + " " + str(depth) + " " + str(nextMove[0]) + str(nextMove[1]) + "\n")

def createNextMovesPlayerStart(ai, file, fromBoard, depth = 1):
    if depth >= maxDepth:
        return

    for i in range(0, 3):
        for j in range(0, 3):
            if fromBoard.GetField(i, j) == 0:
                nextBoard = copy.copy(fromBoard)
                if depth % 2 == 1:
                    nextBoard.SetField(i, j, 2)
                    # Get our next move
                    nextMove = ai.getNextMove(nextBoard)
                    writeMoveToFile(file, depth + 1, nextBoard, nextMove)
                else:
                    nextBoard.SetField(i, j, 1)
                createNextMovesPlayerStart(ai, file, nextBoard, depth + 1)

def createNextMovesOpponentStart(ai, file, fromBoard, depth = 0):
    if depth >= maxDepth:
        return

    for i in range(0, 3):
        for j in range(0, 3):
            if fromBoard.GetField(i, j) == 0:
                nextBoard = copy.copy(fromBoard)
                if depth % 2 == 0:
                    nextBoard.SetField(i, j, 2)
                    # Get our next move
                    nextMove = ai.getNextMove(nextBoard)
                    writeMoveToFile(file, depth + 1, nextBoard, nextMove)
                else:
                    nextBoard.SetField(i, j, 1)
                createNextMovesOpponentStart(ai, file, nextBoard, depth + 1)

def main():
    ai = AI()

    board = Board()
    file = open("ai_first_moves.ai", "w")

    # First we generate our first move in an empty board.
    nextMove = ai.getNextMove(board, 0)

    writeMoveToFile(file, 0, board, nextMove)

    board.SetField(nextMove[0], nextMove[1], 1)
    createNextMovesPlayerStart(ai, file, board)

    newBoard = Board()
    createNextMovesOpponentStart(ai, file, newBoard)

    print("Done")


main()