from os import system
from pynput import keyboard
import time

import aoc_api
from puzzles import historyan_hysteria, red_nosed_reports, mull_it_over, ceres_search, print_queue

selected = 1
in_menu = True
puzzles = {
    'Historian Hysteria': historyan_hysteria.solve,
    'Red-Nosed Reports': red_nosed_reports.solve,
    'Mull It Over': mull_it_over.solve,
    'Ceres Search': ceres_search.solve,
    'Print Queue': print_queue.solve,
}


def clear():
    system('clear')


def show_menu():
    global in_menu
    in_menu = True

    clear()
    print('Advent of Code - 2024')
    print('=================')
    print('Choose puzzle:')
    for i in range(1, len(puzzles) + 1):
        print('{2} Day {0}: {1} {3}'.format(i,
                                            list(puzzles.keys())[i - 1],
                                            ">" if selected == i else " ",
                                            "<" if selected == i else " "))
    print('\n[˄]Up [˅]Down [⏎]Run [T]Test [esc]Exit')


def navigate(direction):
    if in_menu:
        global selected
        selected = selected + direction
        if selected < 1:
            selected = len(puzzles)
        elif selected > len(puzzles):
            selected = 1
        show_menu()


def run(test: bool = False):
    global in_menu
    if not in_menu:
        return
    in_menu = False

    mode = '[TEST] ' if test else ''

    clear()
    print(f'{mode}Puzzle result day {selected}:')
    print('--------------------------------------')

    try:
        puzzle_input = aoc_api.get_puzzle_input(selected, test)
        puzzle_solver = list(puzzles.values())[selected-1]

        start = time.time()
        (solution1, solution2) = puzzle_solver(puzzle_input)
        stop = time.time()

        print("Solution 1:", solution1)
        print("Solution 2:", solution2)

        print('\nExecution time: {}s'.format(round(stop-start, 3)))
    except FileNotFoundError:
        print(f'No test data found for day {selected}!')

    print('\n[<--]Show Menu [esc]Exit')


show_menu()

with keyboard.GlobalHotKeys({
    '<up>': lambda: navigate(-1),
    '<left>': lambda: navigate(-1),
    '<down>': lambda: navigate(1),
    '<right>': lambda: navigate(1),
    '<enter>': run,
    '<backspace>': show_menu,
    't': lambda: run(test=True),
    '<esc>': lambda: keyboard_listener.stop(),
}) as keyboard_listener:
    keyboard_listener.join()

clear()
