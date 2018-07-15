from board import Board
from solver import SudokuSolver
import time

filename = "../resources/hardest-board.txt"

solver = SudokuSolver(filename, 9)
board = solver.board.getBoard().reshape(-1)
cellsLeftToPlace = len(list(filter(lambda cell: cell.getValue()==0, board)))

print("Board to solve: " + filename)
print(solver.board.toString())

start = time.time()
solved = solver.backtracking(solver.board, cellsLeftToPlace)
end = time.time()

if solved:
    print("Board is solved and verified.")
else:
    print("The board is not solvable.")
print("Elapsed time: " + str(end - start) + "s.")

print(solver.board.toString())
