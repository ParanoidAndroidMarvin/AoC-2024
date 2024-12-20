EMPTY = '.'


def solve(puzzle_input):
    disk_map = [int(command) for command in puzzle_input[0]]
    disk_blocks = get_disk_blocks(disk_map)

    disk_blocks_defrag = defrag_disk_blocks(disk_blocks.copy())
    checksum = calculate_checksum(disk_blocks_defrag)

    disk_blocks_defrag2 = defrag_disk_blocks_whole_file(disk_blocks.copy(), disk_map)
    checksum2 = calculate_checksum(disk_blocks_defrag2)

    return checksum, checksum2


def get_disk_blocks(disk_map):
    disk_blocks = []
    for index, command in enumerate(disk_map):
        disk_blocks += [str(int(index/2)) if index % 2 == 0 else EMPTY] * command
    return disk_blocks


def defrag_disk_blocks(disk_blocks):
    while EMPTY in disk_blocks:
        last_block = disk_blocks.pop()
        if last_block == EMPTY:
            continue
        disk_blocks[disk_blocks.index(EMPTY)] = last_block
    return disk_blocks


def calculate_checksum(disk_blocks):
    checksum = 0
    for index, block in enumerate(disk_blocks):
        checksum += index * int(block)
    return checksum


def defrag_disk_blocks_whole_file(disk_blocks, disk_map):
    i = len(disk_blocks)-1
    while i >= 0:
        file_index = disk_blocks[i]

        if file_index == EMPTY:
            i -= 1
            continue

        file_size = get_file_size(file_index, disk_map)
        file_position = i - file_size + 1
        free_space_position = get_free_space_index(disk_blocks, file_size)

        if free_space_position == -1 or free_space_position > file_position:
            i -= file_size
            continue

        move_file(file_index, file_position, file_size, free_space_position, disk_blocks)
        i -= file_size
    return [('0' if block == EMPTY else block) for block in disk_blocks]


def get_file_size(file_index, disk_map):
    return disk_map[int(file_index) * 2]


def get_free_space_index(disk_blocks, size):
    i = 0
    while i < len(disk_blocks):
        if disk_blocks[i] == EMPTY:
            for j in range(size):
                if i + j >= len(disk_blocks):
                    break
                if disk_blocks[i + j] != EMPTY:
                    i += j
                    break
                if j == size - 1:
                    return i
        i += 1
    return -1


def move_file(file_index, file_position, file_size, free_space_position, disk_block):
    for i in range(file_size):
        disk_block[file_position + i] = EMPTY
    for i in range(file_size):
        disk_block[free_space_position + i] = file_index
