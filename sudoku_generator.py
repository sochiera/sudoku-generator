from sudoku_validate import is_sudoku_correct

class Sudoku:
    def __init__(self, n):
        self._rows = []
        for i in range(n):
            self._rows += [[(j+i)%n +1 for j in range(n)]]

    def get_rows(self):
        return self._rows

# what about using matrix?
    def get_columns(self):
        rows = self.get_rows()
        n = len(rows)
        columns = []
        for _ in range(n):
            columns += [[]]
        for i in range(n):
            for j in range(n):
                columns[j].append(rows[i][j])
            # import pdb; pdb.set_trace()

        return columns

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
