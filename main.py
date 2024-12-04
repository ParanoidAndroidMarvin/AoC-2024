from os import system
import keyboard
import time

from puzzles import historyan_hysteria, red_nosed_reports, mull_it_over, ceres_search

selected = 1
in_menu = True
puzzles = {
    'Historian Hysteria': historyan_hysteria.solve,
    'Red-Nosed Reports': red_nosed_reports.solve,
    'Mull It Over': mull_it_over.solve,
    'Ceres Search': ceres_search.solve
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
    print('\n[˄]Up [˅]Down [return]Select [esc]Exit')


def navigate(direction):
    if in_menu:
        global selected
        selected = max(1, selected + direction)
        show_menu()


def select():
    global in_menu
    if not in_menu:
        return
    in_menu = False

    clear()
    print('Puzzle result day {0}:'.format(selected))
    print('---------------------------')

    start = time.time()
    puzzle_solver = list(puzzles.values())[selected-1]
    (solution1, solution2) = puzzle_solver()
    stop = time.time()

    print("Solution 1:", solution1)
    print("Solution 2:", solution2)

    print('\nExecution time: {}s'.format(round(stop-start, 3)))
    print('\n[<--]Show Menu [esc]Exit')


show_menu()
keyboard.add_hotkey('up', lambda: navigate(-1))
keyboard.add_hotkey('left', lambda: navigate(-1))
keyboard.add_hotkey('down', lambda: navigate(+1))
keyboard.add_hotkey('right', lambda: navigate(+1))
keyboard.add_hotkey('enter', select)
keyboard.add_hotkey('backspace', show_menu)
keyboard.wait('esc')
clear()