class Board:
    def __init__(self):
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def GetField(self, row, column):
        return self.__board[row][column]

    def SetField(self, row, column, value):
        self.__board[row][column] = value

    def __copy__(self):
        newBoard = Board()
        newBoard.__board = [row[:] for row in self.__board]
        return newBoard

    def CheckWinState(self):
        # Check rows
        for i in range(0, 3):
            if self.GetField(i, 0) == self.GetField(i, 1) == self.GetField(i, 2) and self.GetField(i, 0) != 0:
                return self.GetField(i, 0) - 1

        # Check columns
        for j in range(0, 3):
            if self.GetField(0, j) == self.GetField(1, j) == self.GetField(2, j) and self.GetField(0, j) != 0:
                return self.GetField(0, j) - 1

        # Check crossing lines
        if self.GetField(0, 0) == self.GetField(1, 1) == self.GetField(2, 2) and self.GetField(0, 0) != 0:
            return self.GetField(0, 0) - 1
        elif self.GetField(0, 2) == self.GetField(1, 1) == self.GetField(2, 0) and self.GetField(0, 2) != 0:
            return self.GetField(0, 2) - 1

        # If the self is full, we call it a draw. To make it easier to write, check if there is an empty square.
        for i in range(0, 3):
            for j in range(0, 3):
                if self.GetField(i, j) == 0:
                    return -1

        # We did not find a free square nor a winner -> it is a draw.
        return 2

    def PrintBoard(self):
        for i in range(0, 3):
            stringToPrint = ""

            for j in range(0, 3):
                if self.GetField(i, j) == 0:
                    stringToPrint += " "
                elif self.GetField(i, j) == 1:
                    stringToPrint += "X"
                else:
                    stringToPrint += "O"

                if j != 2:
                    stringToPrint += "|"
            print(stringToPrint)

            if i != 2:
                print("-----")

    # Serialize (and hash) our board. For our hash we can simply interpret our board as a number with base 3.
    # This will uniquely identify each board and enables us to use a simple dictionary when loading our boards.
    # Note that the board is interpreted in reverse order.
    def SerializeBoard(self):
        hash = 0

        for i in range(0, 3):
            for j in range(0, 3):
                hash += pow(3, (i * 3 + j)) * self.GetField(i, j)

        return hash