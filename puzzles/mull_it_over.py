import aoc_api
import re


def solve():
    puzzle_input = ''.join(aoc_api.fetch_input(3))
    matches1 = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', puzzle_input)
    total1 = sum([int(x) * int(y) for x, y in matches1])

    enabled_puzzle_input = re.sub(r"don't\(\).*?(?:do\(\)|$)", '', puzzle_input)
    matches2 = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', enabled_puzzle_input)
    total2 = sum([int(x) * int(y) for x, y in matches2])

    print("Solution 1:", total1)
    print("Solution 2:", total2)
