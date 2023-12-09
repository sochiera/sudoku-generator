from sudoku_validate import is_sudoku_correct
import numpy as np

class Sudoku:
    def __init__(self, n):
        # what about using numpy array/matrix here too?
        self._rows = []
        for i in range(n):
            self._rows += [[(j+i)%n +1 for j in range(n)]]

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


def generate_sudoku(n):
    return Sudoku(n)

if __name__ == '__main__':
    s = Sudoku(2)
    s.print()
