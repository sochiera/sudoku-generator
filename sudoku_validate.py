from math import floor, sqrt

def check_uniqueness(row):
    numbers = {k for k in row}
    assert(len(numbers) == len(row))

def check_ranges(row):
    for k in row:
        assert 1 <= k and k <= len(row)

def check_rows_count(rows):
    for row in rows:
        assert len(row) == len(rows)


def check_sudoku(sudoku):
    def check_rows(rows):
        check_rows_count(rows)
        for row in rows:
            check_uniqueness(row)
            check_ranges(row)
    check_rows(sudoku.get_rows())
    check_rows(sudoku.get_columns())
    # if sudoku.is_squarable():
    #     check_rows(sudoku.get_squares())


def is_sudoku_correct(sudoku):
    try:
        check_sudoku(sudoku)
    except:
        return False
    return True
