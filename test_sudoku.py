import unittest
from unittest.mock import Mock
from sudoku_generator import Sudoku, generate_sudoku, is_power_of_natural
from sudoku_validate import (
    check_uniqueness,
    check_ranges,
    check_rows_count,
    check_sudoku,
)

class TestSudokuValidate(unittest.TestCase):
    def test_rows_shoule_have_unique_numbers(self):
        check_uniqueness([1,2,3])
        self.assertRaises(AssertionError, check_uniqueness, [1,2,3,2])

    def test_rows_shoule_have_numbers_within_range(self):
        check_ranges([1,2,3])
        check_ranges([1])
        check_ranges([5,3,1,2,4])
        self.assertRaises(AssertionError, check_ranges, [1,2,3,5])
        self.assertRaises(AssertionError, check_ranges, [2])
        self.assertRaises(AssertionError, check_ranges, [0,1,2])

    def test_check_rows_columns_counts(self):
        check_rows_count([[1]])
        check_rows_count([[1,2,3]]*3)
        self.assertRaises(AssertionError, check_rows_count, [[1,2,3]])
        self.assertRaises(AssertionError, check_rows_count, [[1,2,3,4]]*5)

    def test_check_simple_sudoku(self):
        ok_rows = [[1,2,3]]*3
        conflict_rows = [
            [1,2,3],
            [3,1,2],
            [2,3,2]]
        simple_sudoku_mock = Mock(**{
            'get_rows.return_value': ok_rows,
            'get_columns.return_value': ok_rows,
            'get_squares.return_value': ok_rows,
        })
        invalid_rows_sudoku_mock = Mock(**{
            'get_rows.return_value': conflict_rows,
            'get_columns.return_value': ok_rows,
            'get_squares.return_value': ok_rows,
        })
        invalid_columns_sudoku_mock = Mock(**{
            'get_rows.return_value': ok_rows,
            'get_columns.return_value': conflict_rows,
            'get_squares.return_value': ok_rows,
        })
        invalid_squares_sudoku_mock = Mock(**{
            'get_rows.return_value': ok_rows,
            'get_columns.return_value': ok_rows,
            'get_squares.return_value': conflict_rows,
        })
        check_sudoku(simple_sudoku_mock)
        self.assertRaises(AssertionError, check_sudoku, invalid_rows_sudoku_mock)
        self.assertRaises(AssertionError, check_sudoku, invalid_columns_sudoku_mock)
        self.assertRaises(AssertionError, check_sudoku, invalid_squares_sudoku_mock)

    def test_check_squares_uniqueness(self):
        ok_rows = [
            [1,2,3,4],
            [2,3,4,1],
            [3,4,1,2],
            [4,1,2,3],
        ]
        not_ok_squares = [
            [1,1,1,1],
            [2,2,2,2],
            [3,3,3,3],
            [4,4,4,4],
        ]
        sudoku_mock = Mock(**{
            'get_rows.return_value': ok_rows,
            'get_columns.return_value': ok_rows,
            'get_squares.return_value': not_ok_squares,
        })

        self.assertRaises(AssertionError, check_sudoku, sudoku_mock)


class TestSudokuGenerate(unittest.TestCase):
    def test_generate_size_1_sudoku(self):
        self.assertEqual(generate_sudoku(1).get_rows(), [[1]])
        check_sudoku(generate_sudoku(1))

    def test_sudoku_rows_and_collumns_should_match(self):
        s = generate_sudoku(4)
        rows = s.get_rows()
        collumns = s.get_columns()
        self.assertEqual(rows[0][0], collumns[0][0])
        self.assertEqual(rows[1][1], collumns[1][1])
        self.assertEqual(rows[3][3], collumns[3][3])
        self.assertEqual(rows[0][2], collumns[2][0])
        self.assertEqual(rows[3][1], collumns[1][3])

    def test_generate_small_sudoku(self):
        check_sudoku(generate_sudoku(2))
        check_sudoku(generate_sudoku(3))
        check_sudoku(generate_sudoku(5))

    def test_generate_squarable_sudoku(self):
        check_sudoku(generate_sudoku(4))

    def test_generate_one_real_sudoku(self):
        check_sudoku(generate_sudoku(9))


class TestSudoku(unittest.TestCase):
    def test_is_power_of_natural(self):
        powers_of_naturals = [1,4,9,16,25]
        for n in range(1,30):
            self.assertEqual(is_power_of_natural(n), (n in powers_of_naturals))


    def test_sudoku_gets_correct_squares_for_size_4_sudoku(self):
        sudoku = Sudoku([
            [ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12],
            [13, 14, 15, 16]])
        squares = {tuple(sq) for sq in sudoku.get_squares()}
        expected_squares = {
            ( 1,  2,  5,  6),
            ( 3,  4,  7,  8),
            ( 9, 10, 13, 14),
            (11, 12, 15, 16)}
        self.assertEqual(squares, expected_squares)

    def test_sudoku_gets_correct_squares_for_size_9_sudoku(self):
        sudoku = Sudoku([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]])
        squares = {tuple(sq) for sq in sudoku.get_squares()}
        expected_squares = {
            (1, 2, 3, 1, 2, 3, 1, 2, 3),
            (4, 5, 6, 4, 5, 6, 4, 5, 6),
            (7, 8, 9, 7, 8, 9, 7, 8, 9)
        }
        self.assertEqual(squares, expected_squares)


if __name__ == '__main__':
    unittest.main()
