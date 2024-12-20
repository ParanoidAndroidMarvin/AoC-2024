import numpy as np

OPERATORS_PART1 = [
    lambda a, b: a + b,
    lambda a, b: a * b,
]

OPERATORS_PART2 = OPERATORS_PART1 + [
    lambda a, b: int(str(a) + str(b)),
]


def solve(puzzle_input):
    solutions = [int(line.split(':', 1)[0]) for line in puzzle_input]
    equations = [[int(number) for number in line.split(': ')[1].split(' ')] for line in puzzle_input]

    part1 = check_equations_using_operators(equations, solutions, OPERATORS_PART1)
    part2 = check_equations_using_operators(equations, solutions, OPERATORS_PART2)
    return part1, part2


def check_equations_using_operators(equations, solutions, operators):
    total_correct_solutions = 0
    for i in range(len(equations)):
        if check_equation(equations[i], solutions[i], operators):
            total_correct_solutions += solutions[i]
    return total_correct_solutions


def check_equation(equation, expected_solution, operators):
    equation = equation.copy()
    if len(equation) == 1:
        if equation[0] == expected_solution:
            return True
        else:
            return False

    first_value = equation.pop(0)
    for operator in operators:
        new_equation = equation.copy()
        new_equation[0] = operator(first_value, new_equation[0])
        if check_equation(new_equation, expected_solution, operators):
            return True
    return False
