import unittest
from unittest.mock import Mock
from sudoku_generator import generate_sudoku
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
        })
        invalid_rows_sudoku_mock = Mock(**{
            'get_rows.return_value': conflict_rows,
            'get_columns.return_value': ok_rows,
        })
        invalid_columns_sudoku_mock = Mock(**{
            'get_rows.return_value': ok_rows,
            'get_columns.return_value': conflict_rows,
        })
        check_sudoku(simple_sudoku_mock)
        self.assertRaises(AssertionError, check_sudoku, invalid_rows_sudoku_mock)
        self.assertRaises(AssertionError, check_sudoku, invalid_columns_sudoku_mock)

class TestSudokuGenerate(unittest.TestCase):
    def test_generate_size_1_sudoku(self):
        self.assertEqual(generate_sudoku(1).get_rows(), [[1]])
        check_sudoku(generate_sudoku(1))


    def test_generate_size_2_sudoku(self):
        check_sudoku(generate_sudoku(2))

if __name__ == '__main__':
    unittest.main()
