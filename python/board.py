# -*- coding: utf-8 -*-
import numpy as np
from cell import Cell

class Board:
    '''
    Board representation of a sudoku puzzle.
    A board consists of Cell-objects.
    '''

    def __init__(self, filename):
        self.board = self.readFile(filename)
        self.SIZE = self.board.shape[0]

    def readFile(self, filename):
        board = []
        numrows = 0
        numcols = 0

        for line in open(filename).readlines():
            numcols = 0
            for ch in line.strip("\n"):
                try:
                    input = int(ch)
                    if (numcols > 9 or 0 > input or input > 9):
                        raise Exception

                    isEditable = input == 0
                    board.append(Cell(int(ch), numrows, numcols, isEditable))
                    numcols += 1
                except:
                    raise Exception(
                        "Error reading input in file \"" + filename + "\"")
            numrows += 1

        board = np.reshape(board, (numrows, numcols))
        return board

    def getBoard(self):
        return self.board

    def getCell(self, row, col):
        return self.board[row][col]

    def setCellValue(self, cell, value):
        cell.setValue(value)
        self.updateConflictsOnBoard()

    def isCellInConflict(self, cell):
        if cell.getValue() == 0:
            return False

        # check rows and columns
        for i in range(9):
            colCell = self.getCell(cell.row, i)
            rowCell = self.getCell(i, cell.col)

            if not (colCell == cell):
                if colCell.getValue() == cell.getValue():
                    return True

            if not (rowCell == cell):
                if rowCell.getValue() == cell.getValue():
                    return True

        # check inner 3x3
        startRow = cell.row - cell.row % 3
        startCol = cell.col - cell.col % 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                c = self.getCell(i, j)
                if not (c == cell):
                    if c.getValue() == cell.getValue():
                        return True

        return False

    def updateConflictsOnBoard(self):
        ''' Updates the inConflict-variable of the cells on the board. '''
        cells = self.board.reshape(-1)
        for cell in cells:
            cell.setInConflict(self.isCellInConflict(cell))


    def toString(self):
        string = "\n"
        for row in range(self.SIZE):
            if row % 3 == 0 and row != 0:
                string += " - " * 14 + "\n"
            for col in range(self.SIZE):
                if col % 3 == 0 and col != 0:
                    string += " | "
                if (not self.board[row][col].isEditable):
                    string += " " + str(self.board[row][col].getValue()) + "* "
                else:
                    string += " " + str(self.board[row][col].getValue()) + "  "
            string += "\n"
        return string
