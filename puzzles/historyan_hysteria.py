import aoc_api
import numpy as np


def solve():
    puzzle_input = aoc_api.fetch_input(1)
    complete_list = np.array([entry.split("   ") for entry in puzzle_input]).astype(int)
    list1 = np.sort(complete_list[:, 0])
    list2 = np.sort(complete_list[:, 1])

    distance = np.sum(np.abs(np.subtract(list1, list2)))

    distance2 = np.sum([value * np.count_nonzero(list2 == value) for value in list1])

    print("Solution 1: ", distance)
    print("Solution 2: ", distance2)
