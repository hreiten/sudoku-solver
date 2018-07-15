# -*- coding: utf-8 -*-
from cell import Cell
import numpy as np


class Board:
    ''' Board representation of a sudoku puzzle.
        A board consists of Cell-objects.
    '''

    def __init__(self, filename, size):
        ''' Initialize by loading sudoku board from file
        @param filename The name of the txt-file containing the sudoku puzzle
        @param size The size of the sudoku board (for validational purposes)
        '''
        self.SIZE = size
        self.BOARD = self.readFile(filename)

    def readFile(self, filename):
        ''' Reads file and loads a new sudoku board '''
        board = []
        numrows = 0
        numcols = 0

        for line in open(filename).readlines():
            numcols = 0
            for ch in line.strip("\n"):
                try:
                    input = int(ch)
                    if (numcols > self.SIZE or 0 > input or input > 9):
                        raise Exception

                    isEditable = input == 0
                    board.append(Cell(input, numrows, numcols, isEditable))
                    numcols += 1
                except:
                    raise Exception(
                        "Error reading input in file \"" + filename + "\"")
            numrows += 1

        if numrows != self.SIZE or numcols != self.SIZE:
            raise Exception(
                "Illegal input in file. #Rows and/or #Columns != " + self.SIZE)

        board = np.reshape(board, (numrows, numcols))
        return board

    def getBoard(self):
        return self.BOARD

    def getCell(self, row, col):
        return self.BOARD[row][col]

    def isCellInConflict(self, cell):
        ''' Decides if a cell is in conflict with other cells '''
        if cell.getValue() == 0:
            return False

        if cell.getValue() in [c.getValue() for c in cell.ASSOCIATED_CELLS]:
            return True

        return False

    def getRow(self, row):
        ''' Returns all cells in given row '''
        return self.BOARD[row, :]

    def getCol(self, col):
        ''' Returns all cells in given column '''
        return self.BOARD[:, col]

    def getInnerBox(self, cell):
        ''' Returns all cells in inner 3x3 box matrix '''
        startRow = cell.ROW - cell.ROW % 3
        startCol = cell.COL - cell.COL % 3
        return self.BOARD[startRow:startRow + 3, startCol:startCol + 3]

    def toString(self):
        ''' Returns a string representation of the board '''

        string = "\n"
        for row in range(self.SIZE):
            if row % 3 == 0 and row != 0:
                string += " - " * 14 + "\n"
            for col in range(self.SIZE):
                if col % 3 == 0 and col != 0:
                    string += " | "
                if (not self.getCell(row,col).IS_EDITABLE):
                    string += " " + str(self.getCell(row,col).getValue()) + "* "
                else:
                    string += " " + str(self.getCell(row,col).getValue()) + "  "
            string += "\n"
        return string
