import re

mul_regex = r'mul\((\d{1,3}),(\d{1,3})\)'
disable_regex = r"don't\(\).*?(?:do\(\)|$)"


def solve(puzzle_input):
    puzzle_input = ''.join(puzzle_input)
    matches1 = re.findall(mul_regex, puzzle_input)
    total1 = sum([int(x) * int(y) for x, y in matches1])

    enabled_puzzle_input = re.sub(disable_regex, '', puzzle_input)
    matches2 = re.findall(mul_regex, enabled_puzzle_input)
    total2 = sum([int(x) * int(y) for x, y in matches2])

    return total1, total2
