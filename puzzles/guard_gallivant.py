import numpy as np

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'
INTERSECTION = '+'

GUARD = '^'
OBSTACLE = '#'
EMPTY = '.'
PATHS = [UP, DOWN, LEFT, RIGHT, INTERSECTION]

DIRECTIONS = [
    (-1, 0, UP),
    (0, 1, RIGHT),
    (1, 0, DOWN),
    (0, -1, LEFT)
]


class EndlessLoopException(Exception):
    pass


def solve(guard_map):
    guard_map = np.array([list(line) for line in guard_map])
    return solve_part_1(guard_map), solve_part_2(guard_map)


def solve_part_1(guard_map):
    guard_map = np.copy(guard_map)
    map_shape = np.shape(guard_map)
    x, y = np.where(guard_map == GUARD)

    current_direction = 0
    current_position = (x[0], y[0])

    step = 0

    while check_border(map_shape, current_position, DIRECTIONS[current_direction]):
        step += 1
        if step % 10000 == 0:
            # IDK what the fuck is happening here... but at this point it is also an endless loop (maybe always running back and forth)
            print(guard_map)
            raise EndlessLoopException
        if detect(guard_map, current_position, DIRECTIONS[current_direction]):
            current_direction = rotate(guard_map, current_position, current_direction)
        else:
            current_position = move(guard_map, current_position, DIRECTIONS[current_direction])
    return np.isin(guard_map, PATHS).sum() + 1


def solve_part_2(guard_map):
    map_shape = np.shape(guard_map)
    endless_loop_count = 0
    for i in range(map_shape[0]):
        for j in range(map_shape[1]):
            if guard_map[i][j] != EMPTY:
                continue
            adjusted_guard_map = np.copy(guard_map)
            adjusted_guard_map[i][j] = OBSTACLE
            try:
                solve_part_1(adjusted_guard_map)
            except EndlessLoopException:
                endless_loop_count += 1
    return endless_loop_count


def check_border(map_shape, position, direction):
    new_position = add_tuples(position, direction)
    return 0 <= new_position[0] < map_shape[0] and 0 <= new_position[1] < map_shape[1]


def move(guard_map, position, direction) -> (int, int):
    mark_path(guard_map, position, direction[2])
    return add_tuples(position, direction)


def mark_path(guard_map, position, marker):
    if guard_map[position[0]][position[1]] not in PATHS:
        guard_map[position[0]][position[1]] = marker
    elif guard_map[position[0]][position[1]] == INTERSECTION or guard_map[position[0]][position[1]] != marker:
        guard_map[position[0]][position[1]] = INTERSECTION
    else:
        raise EndlessLoopException


def rotate(guard_map, position, current_direction):
    mark_path(guard_map, position, INTERSECTION)
    new_direction = current_direction + 1
    if new_direction > len(DIRECTIONS) - 1:
        new_direction = 0
    return new_direction


def detect(guard_map, position, direction):
    next_field = add_tuples(position, direction)
    return guard_map[next_field[0]][next_field[1]] == OBSTACLE


def add_tuples(first, second):
    return first[0] + second[0], first[1] + second[1]
