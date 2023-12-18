from sudoku_validate import is_sudoku_correct
import numpy as np
from math import floor, sqrt

def is_power_of_natural(n):
    k = floor(sqrt(n))
    return k*k == n

class Sudoku:
    def __init__(self, rows):
        # what about using numpy array/matrix here too?
        self._rows = rows

    def is_squarable(self):
        return is_power_of_natural(len(self._rows))

    def get_rows(self):
        return self._rows

    def get_columns(self):
        matrix = np.array(self._rows)
        return matrix.transpose().tolist()

    def get_squares(self):
        n = len(self._rows)
        k = floor(sqrt(n))
        if k*k != n:
            return []
        squares = []
        for i in range(k):
            squares += [[]]
            for j in range(k):
                squares[i] += [[]]
        for i in range(n):
            for j in range(n):
                squares[floor(i/k)][floor(j/k)].append(self._rows[i][j])
        return [e for square in squares for e in square]

    def print(self):
        rows = self.get_rows()
        n = len(rows)
        print('-' * (n*4 + 1))
        for r in self.get_rows():
            print("| " + ' | '.join(str(k) for k in r) + " |")
            print('-' * (n*4 + 1))

    def __str__(self):
        return str(self.get_rows())

class SudokuGenerator:
    def __init__(self, n):
        self._n = n

    def generate(self):
        n = self._n
        rows = []
        for i in range(n):
            rows += [[(j+i)%n +1 for j in range(n)]]
        if n == 4:
            rows[1],rows[2] = rows[2],rows[1]
        return Sudoku(rows)

def generate_sudoku(n):
    sg = SudokuGenerator(n)
    return sg.generate()
