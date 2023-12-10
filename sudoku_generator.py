from sudoku_validate import is_sudoku_correct
import numpy as np

class Sudoku:
    def __init__(self, rows):
        # what about using numpy array/matrix here too?
        self._rows = rows

    def get_rows(self):
        return self._rows

    def get_columns(self):
        matrix = np.array(self._rows)
        return matrix.transpose().tolist()

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
        return Sudoku(rows)

def generate_sudoku(n):
    sg = SudokuGenerator(n)
    return sg.generate()
