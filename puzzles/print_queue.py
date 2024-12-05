import math
from collections import defaultdict, deque


def solve(puzzle_input):
    split_index = puzzle_input.index('')
    rules = [[int(x) for x in rule.split('|')] for rule in puzzle_input[:split_index]]
    updates = [[int(x) for x in update.split(',')] for update in puzzle_input[split_index+1:]]

    valid_updates_sum = sum_up_valid_updates(updates, rules)
    fixed_updates_sum = sum_up_fixed_updates(updates, rules)

    return valid_updates_sum, fixed_updates_sum


def sum_up_fixed_updates(updates: list, rules: list) -> int:
    return sum([get_update_value(fix_update(update, rules)) for update in updates if not validate_update(update, rules)])


def fix_update(update: list, rules: list) -> list:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    relevant_rules = [rule for rule in rules if (rule[0] in update and rule[1] in update)]
    for first, second in relevant_rules:
        graph[first].append(second)
        in_degree[second] += 1
        if first not in in_degree:
            in_degree[first] = 0

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    update = []

    while queue:
        node = queue.popleft()
        update.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return update


def sum_up_valid_updates(updates: list, rules: list) -> int:
    return sum([get_update_value(update) for update in updates if validate_update(update, rules)])


def get_update_value(update: list) -> int:
    return update[int(math.floor((len(update))/2))]


def validate_update(update: list, rules: list) -> bool:
    for rule in rules:
        if (rule[0] in update and rule[1] in update) and update.index(rule[1]) < update.index(rule[0]):
            return False
    return True
