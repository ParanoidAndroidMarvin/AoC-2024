import numpy as np

import aoc_api

XMAS_PATTERN_1 = np.array([['X', 'M', 'A', 'S']])
XMAS_PATTERN_2 = np.array([['S', 'A', 'M', 'X']])
XMAS_PATTERN_3 = np.array([['X'],
                           ['M'],
                           ['A'],
                           ['S']])
XMAS_PATTERN_4 = np.array([['S'],
                           ['A'],
                           ['M'],
                           ['X']])
XMAS_PATTERN_5 = np.array([['X', '', '', ''],
                           ['', 'M', '', ''],
                           ['', '', 'A', ''],
                           ['', '', '', 'S']])
XMAS_PATTERN_6 = np.array([['S', '', '', ''],
                           ['', 'A', '', ''],
                           ['', '', 'M', ''],
                           ['', '', '', 'X']])
XMAS_PATTERN_7 = np.array([['', '', '', 'S'],
                           ['', '', 'A', ''],
                           ['', 'M', '', ''],
                           ['X', '', '', '']])
XMAS_PATTERN_8 = np.array([['', '', '', 'X'],
                           ['', '', 'M', ''],
                           ['', 'A', '', ''],
                           ['S', '', '', '']])
XMAS_PATTERNS = [XMAS_PATTERN_1, XMAS_PATTERN_2, XMAS_PATTERN_3, XMAS_PATTERN_4, XMAS_PATTERN_5, XMAS_PATTERN_6, XMAS_PATTERN_7, XMAS_PATTERN_8]

MAS_PATTERN_1 = np.array([['M', '', 'M'],
                          ['', 'A', ''],
                          ['S', '', 'S']])
MAS_PATTERN_2 = np.array([['M', '', 'S'],
                          ['', 'A', ''],
                          ['M', '', 'S']])
MAS_PATTERN_3 = np.array([['S', '', 'M'],
                          ['', 'A', ''],
                          ['S', '', 'M']])
MAS_PATTERN_4 = np.array([['S', '', 'S'],
                          ['', 'A', ''],
                          ['M', '', 'M']])
MAS_PATTERNS = [MAS_PATTERN_1, MAS_PATTERN_2, MAS_PATTERN_3, MAS_PATTERN_4]


def solve():
    puzzle_input = np.array([list(line) for line in aoc_api.fetch_input(4)])
    xmas_count = count_occurrence_of_sub_arrays(puzzle_input, XMAS_PATTERNS)
    mas_count = count_occurrence_of_sub_arrays(puzzle_input, MAS_PATTERNS)

    return xmas_count, mas_count

def count_occurrence_of_sub_arrays(array, sub_arrays) -> int:
    count = 0
    for sub_array in sub_arrays:
        count += count_occurrence_of_sub_array(array, sub_array)
    return count


def count_occurrence_of_sub_array(array: np.array, subarray: np.array) -> int:
    if subarray.ndim == 1:
        subarray = subarray.reshape(-1, 1)

    count = 0
    (x, y) = array.shape
    (xs, ys) = subarray.shape

    for xd in range(x - (xs - 1)):
        for yd in range(y - (ys - 1)):
            if check_for_sub_array(array, subarray, xd, yd):
                count += 1

    return count


def check_for_sub_array(array, subarray, x, y) -> bool:
    (xs, ys) = subarray.shape
    for xd in range(xs):
        for yd in range(ys):
            if subarray[xd, yd] and array[x + xd, y + yd] != subarray[xd, yd]:
                return False
    return True
