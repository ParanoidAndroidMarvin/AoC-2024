from os import system
from pynput import keyboard
import time

import aoc_api
from puzzles import historyan_hysteria, red_nosed_reports, mull_it_over, ceres_search, print_queue, guard_gallivant, bridge_repair

selected_day = 1
solution = None

in_menu = True
puzzles = {
    'Historian Hysteria': historyan_hysteria.solve,
    'Red-Nosed Reports': red_nosed_reports.solve,
    'Mull It Over': mull_it_over.solve,
    'Ceres Search': ceres_search.solve,
    'Print Queue': print_queue.solve,
    'Guard Gallivant': guard_gallivant.solve,
    'Bridge Repair': bridge_repair.solve,
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
                                            ">" if selected_day == i else " ",
                                            "<" if selected_day == i else " "))
    print('\n[˄]Up [˅]Down [⏎]Run [T]Test [esc]Exit')


def navigate(direction):
    if in_menu:
        global selected_day
        selected_day = selected_day + direction
        if selected_day < 1:
            selected_day = len(puzzles)
        elif selected_day > len(puzzles):
            selected_day = 1
        show_menu()


def run(test: bool = False):
    global in_menu
    if not in_menu:
        return
    in_menu = False

    mode = '[TEST] ' if test else ''

    clear()
    print(f'{mode}Puzzle result day {selected_day}:')
    print('--------------------------------------')

    try:
        global solution
        puzzle_input = aoc_api.get_puzzle_input(selected_day, test)
        puzzle_solver = list(puzzles.values())[selected_day - 1]

        start = time.time()
        solution = puzzle_solver(puzzle_input)
        stop = time.time()

        print("Solution 1:", solution[0])
        print("Solution 2:", solution[1])

        print('\nExecution time: {}s'.format(round(stop-start, 3)))
    except FileNotFoundError:
        print(f'No test data found for day {selected_day}!')

    if test:
        print('\n[<--]Menu [esc]Exit')
    else:
        print('\n[<--]Menu [cmd+shift+1]Submit Part 1 [cmd+shift+2]Submit Part 2 [esc]Exit')


def submit(part: int):
    if (not solution or
            in_menu):
        return

    clear()
    print(aoc_api.submit_solution(selected_day, part, solution[part-1]))
    print('\n[<--]Menu [esc]Exit')


show_menu()

with keyboard.GlobalHotKeys({
    '<up>': lambda: navigate(-1),
    '<left>': lambda: navigate(-1),
    '<down>': lambda: navigate(1),
    '<right>': lambda: navigate(1),
    '<cmd>+<enter>': lambda: run(test=True),
    '<enter>': run,
    '<backspace>': show_menu,
    '<cmd>+<shift>+1': lambda: submit(1),
    '<cmd>+<shift>+2': lambda: submit(2),
    '<esc>': lambda: keyboard_listener.stop(),
}) as keyboard_listener:
    keyboard_listener.join()

clear()
