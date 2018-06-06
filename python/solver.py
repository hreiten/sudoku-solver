import numpy as np
from board import Board

class SudokuSolver:
    '''Contains methods for solving a Sudoku puzzle.'''

    def __init__(self, filename):
        # load sudoku board
        self.board = Board(filename)

        # add constraints to the cells
        for elem in self.board.getBoard().reshape(-1):
            elem.setPossibleValues(
                self.getPossibleValuesForCell(elem, self.board))

    def getPossibleValuesForCell(self, cell, board):
        '''
        Returns which values are possible for a cell to have given a
        board configuration.
        '''

        if not cell.isEditable:
            return [cell.getValue()]

        possibleValues = range(1, 10)

        # check rows and columns
        for i in range(9):
            colCell = board.getCell(cell.row, i)
            rowCell = board.getCell(i, cell.col)

            if not (colCell == cell) and colCell.getValue() in possibleValues:
                possibleValues.remove(colCell.getValue())

            if not (rowCell == cell) and rowCell.getValue() in possibleValues:
                possibleValues.remove(rowCell.getValue())

        # check inner 3x3
        startRow = cell.row - cell.row % 3
        startCol = cell.col - cell.col % 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                c = board.getCell(i, j)
                if not (c == cell) and c.getValue() in possibleValues:
                    possibleValues.remove(c.getValue())

        return possibleValues

    def checkBoard(self, board):
        cells = board.getBoard().reshape(-1)
        for cell in cells:
            if (cell.getValue() == 0 or cell.inConflict):
                return False

        return True

    def backtracking(self, board):
        cells = board.getBoard().reshape(-1)
        lastCell = cells[0]
        for cell in cells:
            lastCell = cell
            if cell.getValue() != 0 or not cell.isEditable:
                continue

            for val in cell.possibleValues:
                board.setCellValue(cell, val)
                if (cell.inConflict):
                    board.setCellValue(cell, 0)
                    continue

                if self.checkBoard(board) or self.backtracking(board):
                    return True

            break

        # backtrack
        board.setCellValue(lastCell, 0)
