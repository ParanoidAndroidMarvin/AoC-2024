import aoc_api
import numpy as np


def solve():
    puzzle_input = aoc_api.fetch_input(2)
    reports = [[int(entry) for entry in line.split(' ')] for line in puzzle_input]
    safe_reports = sum([1 for report in reports if check_levels(report, False)])
    safe_reports2 = sum([1 for report in reports if check_levels(report, True)])

    return safe_reports, safe_reports2


def check_levels(levels, dampener_available):
    increase = levels[0] < levels[1]
    for i in range(len(levels)-1):
        dif = levels[i] - levels[i+1]
        if (abs(dif) > 3) or (increase and dif >= 0) or (not increase and dif <= 0):
            if dampener_available:
                for i in range(len(levels)):
                    dampened_levels = levels.copy()
                    del dampened_levels[i]
                    if check_levels(dampened_levels, False):
                        return True
                return False
            return False
    return True
