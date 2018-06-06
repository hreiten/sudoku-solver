from board import Board
from solver import SudokuSolver
import time

filename = "../resources/easy-board.txt"

solver = SudokuSolver(filename)

print "Board to solve:"
print solver.board.toString()

start = time.time()
solved = solver.backtracking(solver.board)
end = time.time()

if solved:
    print "Solved in " + str(end - start) + "s."
else:
    print "The board is not solvable."

print solver.board.toString()
