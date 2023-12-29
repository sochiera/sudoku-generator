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

    def pretty_printable(self):
        rows = self.get_rows()
        n = len(rows)
        output = ""
        output += ('-' * (n*4 + 1)) + "\n"
        for r in self.get_rows():
            output += ("| " + ' | '.join(str(k) for k in r) + " |") + "\n"
            output += ('-' * (n*4 + 1)) + "\n"
        return output

    def __str__(self):
        return self.pretty_printable()

class SudokuGenerator:
    def __init__(self, n):
        self._n = n

    def generate(self):
        n = self._n
        rows = []
        for _ in range(n):
            rows += [[0]*n]
        return Sudoku(rows)

def generate_sudoku(n):
    sg = SudokuGenerator(n)
    return sg.generate()

if __name__ == '__main__':
    print(generate_sudoku(9))
