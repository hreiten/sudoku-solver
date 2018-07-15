import numpy as np
from board import Board
from time import sleep


class SudokuSolver:
    '''
    Class to solve any sudoku puzzle (with integers only)
    '''

    def __init__(self, filename, size):
        ''' Initialize by reading and loading a sudoku board.
        @param filename The txt-file containing the sudoku puzzle.
        @param size The size of the sudoku board
        '''
        self.board = Board(filename, size)

        for i in range(size**2):
            cell = self.board.getCell(int(i/size), i%size)
            cell.setAssociatedCells(self.getAssociatedCellsForCell(cell, self.board))
            cell.setPossibleValues(self.getPossibleValuesForCell(cell))

    def getAssociatedCellsForCell(self, cell, board):
        ''' Decides which cells are "associated" with the input cell, i.e.
        cells in same row, same column and inner 3x3 matrix.
        @param cell The cell to calculate relative to.
        @param board The board object with cells
        @return All distinct cells associated with cell
        '''
        rowCells = board.getRow(cell.ROW)
        colCells = board.getCol(cell.COL)
        innerBox = board.getInnerBox(cell).reshape(-1)

        allCells = np.concatenate((rowCells, colCells, innerBox))
        distinctAssociatedCells = []
        for c in allCells:
            if c not in distinctAssociatedCells and c != cell:
                distinctAssociatedCells.append(c)

        return distinctAssociatedCells

    def getPossibleValuesForCell(self, cell):
        ''' Compares a cell to its associated cells and decides which values are
        possible to put there in accordance with Sudoku-rules.
        @param cell The cell to find possible values for
        @return The possible values a cell can have '''

        if not cell.IS_EDITABLE:
            return [cell.getValue()]

        allValues = [c.getValue() for c in cell.ASSOCIATED_CELLS]
        possibleValues = [x for x in range(1, 10) if x not in allValues]

        return possibleValues

    def checkBoard(self, board):
        ''' Decides if given board is complete without errors.
        @param board The board object to check
        @return True if board is correct.
        '''
        for i in range(board.SIZE**2):
            row = int(i / board.SIZE)
            col = i % board.SIZE
            cell = board.getCell(row, col)
            if cell.getValue() == 0 or board.isCellInConflict(cell):
                return False
        return True

    def backtracking(self, board, cellsLeftToPlace):
        ''' Backtracking algorithm to solve a given sudoku board.
        @param board The board to solve
        @param cellsLeftToPlace The number of cells left to decide
        @return True if board can be solved.
        '''

        if cellsLeftToPlace == 0:
            return self.checkBoard(board)

        for i in range(0, board.SIZE**2):
            row = int(i / board.SIZE)
            col = i % board.SIZE
            cell = board.getCell(row, col)

            if cell.getValue() != 0 or not cell.IS_EDITABLE:
                continue

            # update possible values for cell
            possVals = self.getPossibleValuesForCell(cell)

            for val in possVals:
                cell.setValue(val)
                if board.isCellInConflict(cell):
                    cell.setValue(0)  # reset and try next possible value
                    continue

                if self.backtracking(board, cellsLeftToPlace - 1):
                    return True

            break

        # backtrack
        cell.setValue(0)
