class Cell:
    '''
    Defines the elements of a grid to be used in a Sudoku board.
    '''

    def __init__(self, value, row, col, isEditable=True):
        self.value = value
        self.isEditable = isEditable
        self.row, self.col = row, col
        self.inConflict = False

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

    def isEditable(self):
        return self.isEditable

    def setPossibleValues(self, possibleValues):
        self.possibleValues = possibleValues

    def setInConflict(self, inConflict):
        self.inConflict = inConflict

    def __eq__(self, other):
        return self.value == other.value and self.row == other.row and self.col == other.col
