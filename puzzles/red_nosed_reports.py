import aoc_api


def solve(puzzle_input):
    reports = [[int(entry) for entry in line.split(' ')] for line in puzzle_input]
    safe_reports = sum([1 for report in reports if check_levels(report, False)])
    safe_reports2 = sum([1 for report in reports if check_levels(report, True)])

    return safe_reports, safe_reports2


def check_levels(levels, dampener_available):
    is_sorted = levels == sorted(levels) or levels == sorted(levels, reverse=True)
    for i in range(len(levels)-1):
        diff = abs(levels[i] - levels[i+1])
        if not is_sorted or (diff > 3) or (diff == 0):
            if dampener_available:
                for j in range(len(levels)):
                    dampened_levels = levels.copy()
                    del dampened_levels[j]
                    if check_levels(dampened_levels, False):
                        return True
            return False
    return True
