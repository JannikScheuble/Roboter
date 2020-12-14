from board import*
import copy

class Node:
    def __init__(self):
        self.children = []
        self.board = None
        self.nextMove = (-1, -1)
        self.value = 0

    def AddChild(self, child):
        self.children.append(child)

    def GetChildren(self):
        return self.children

class AI:
    def __init__(self, precalculatedDecisionsPath = ""):
        self.precalculatedMoves = {}

        if precalculatedDecisionsPath == "":
            return

        file = open(precalculatedDecisionsPath)
        if file:
            print("Loading precalculated decisions...")

            line = file.readline()

            while line != "":
                lineContents = line.split(" ")
                self.precalculatedMoves[int(lineContents[0])] = (int(lineContents[2][0]), int(lineContents[2][1]))

                line = file.readline()

            print("Precalculated decisions loaded!")

    def getNextMove(self, board, player=0):
        # First try to get our next move from our precalculated decisions.
        serializedBoard = board.SerializeBoard()
        precalculatedMove = self.precalculatedMoves.get(serializedBoard)
        if precalculatedMove != None:
            return precalculatedMove

        root = AI.generateMiniMaxTree(board, player)

        maxValueNode = None
        maxValue = -1
        for child in root.GetChildren():
            if maxValueNode == None:
                maxValueNode = child
                maxValue = child.value
            elif child.value > maxValue:
                maxValueNode = child
                maxValue = child.value

        return maxValueNode.nextMove

    def generateMiniMaxTree(board, player):#
        root = Node()
        root.board = board
        AI.generateNextNodes(player, root)
        AI.evaluateTree(player, root)

        maxChild = None
        for child in root.GetChildren():
            if maxChild == None:
                maxChild = child
            elif maxChild.value < child.value:
                maxChild = child

        return root

    def generateNextNodes(player, fromNode):
        # If the board is already played to its end, we can end the tree generation here
        if fromNode.board.CheckWinState() != -1:
            return

        for i in range(0, 3):
            for j in range(0, 3):
                if fromNode.board.GetField(i, j) == 0:
                    nextNode = Node()
                    nextNode.board = copy.copy(fromNode.board)
                    nextNode.board.SetField(i, j, player + 1)
                    nextNode.nextMove = (i, j)
                    fromNode.AddChild(nextNode)

        for child in fromNode.GetChildren():
            AI.generateNextNodes((player + 1) % 2, child)

    def evaluateTree(player, root):
        AI.evaluateNode(player, root)

    def evaluateNode(player, node):
        winState = node.board.CheckWinState()

        # If the board does not have a win state yet, continue looking into the children
        if winState == -1:
            # If we are the player currently being looked for, we have to look for a maximum -> initialize with minimum
            minOrMax = -1

            # If we are not the player currently being looked for, we have to look for a minimum -> initialize with maximum
            if player != 0:
                minOrMax = 1

            for child in node.GetChildren():
                AI.evaluateNode((player + 1) % 2, child)
                # Find the min of the nodes
                if player != 0:
                    if child.value < minOrMax:
                        minOrMax = child.value
                # Find the max of the nodes
                else:
                    if child.value > minOrMax:
                        minOrMax = child.value

            node.value = minOrMax

        else:
            if winState == 2:
                node.value = 0
            elif winState == 0: # We are player 0
                node.value = 1
            else:
                node.value = -1
