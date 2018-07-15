class Cell:
    '''
    Defines the elements of a grid to be used in a Sudoku board.
    '''
    IS_EDITABLE = True
    IN_CONFLICT = False
    ASSOCIATED_CELLS = []
    POSSIBLE_VALUES = []

    def __init__(self, value, row, col, isEditable):
        self.VALUE = value
        self.IS_EDITABLE = isEditable
        self.ROW = row
        self.COL = col

    def getValue(self):
        return self.VALUE

    def setValue(self, newValue):
        self.VALUE = newValue

    def getAllAssociatedCells(self):
        return self.ASSOCIATED_CELLS

    def setInConflict(self, isInConflict):
        self.IN_CONFLICT = isInConflict

    def setAssociatedCells(self, cells):
        self.ASSOCIATED_CELLS = cells

    def setPossibleValues(self, possibleValues):
        self.POSSIBLE_VALUES = possibleValues

    def __eq__(self, other):
        return self.VALUE == other.VALUE and self.ROW == other.ROW and self.COL == other.COL

    def compareTo(self,other):
        return len(self.POSSIBLE_VALUES) - len(other.POSSIBLE_VALUES)
