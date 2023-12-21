# File for day 18 of AoC 2023
# Written by Joshua Yeaton on 12/18/2023

import queue

def parse_line(line):
    line = line.strip()
    split_line = line.split()
    return (split_line[0], int(split_line[1]), split_line[2])

def parse_line_pt_2(line):
    line = line.strip()
    split_line = line.split()
    instr = split_line[2].strip('()')
    dir_num = instr[-1]
    hex_num = instr[1:-1]
    hex_num = '0x' + hex_num
    if dir_num == '0':
        dir = 'R'
    elif dir_num == '1':
        dir = 'D'
    elif dir_num == '2':
        dir = 'L'
    elif dir_num == '3':
        dir = 'U'
    return (dir, int(hex_num, 0))

def get_adj(coord):
    return [(coord[0], coord[1] + 1),
            (coord[0], coord[1] - 1),
            (coord[0] + 1, coord[1]),
            (coord[0] - 1, coord[1])]

def add_trench(cur_loc, dir, dist, trench_locs):
    if dir == 'R':
        delta = (0, 1)
    elif dir == 'L':
        delta = (0,-1)
    elif dir == 'U':
        delta = (-1, 0)
    elif dir == 'D':
        delta = (1, 0)
    for i in range(1, dist + 1):
        cur_loc = (cur_loc[0] + delta[0], cur_loc[1] + delta[1])
        trench_locs.update({cur_loc:1})
    return cur_loc

def fill_trench(trench_locs, min_row, min_col, max_row, max_col):
    fill_queue = queue.Queue()
    # Find first filled location in the first row
    c = 0
    while((0, c) not in trench_locs):
        c += 1
        # Grab the first inside loc by moving diagonally
    first_inside = (1, c + 1)
    fill_queue.put(first_inside)
    while (not fill_queue.empty()):
        cur_node = fill_queue.get()
        if cur_node not in trench_locs:
            trench_locs.update({cur_node:1})
            adj_nodes = get_adj(cur_node)
            for n in adj_nodes:
                fill_queue.put(n)
    return trench_locs


if __name__ == '__main__':
    file_name = 'data.txt'
    file_name = 'data-test.txt'

    f = open(file_name)

    trench_locs = {}
    cur_loc = (0,0)
    trench_locs.update({cur_loc:1})

    for line in f:
        (dir, dist, color) = parse_line(line)
        # (dir, dist) = parse_line_pt_2(line)
        cur_loc = add_trench(cur_loc, dir, dist, trench_locs)
    

    f.close()

    max_row = 0
    max_col = 0
    min_row = 0
    min_col = 0
    for entry in trench_locs:
        if entry[0] > max_row:
            max_row = entry[0]
        if entry[1] > max_col:
            max_col = entry[1]
        if entry[0] < min_row:
            min_row = entry[0]
        if entry[1] < min_col:
            min_col = entry[1]

    # for i in range(min_row, max_row + 1):
    #     for j in range(min_col, max_col + 1):
    #         if (i,j) in trench_locs:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()

    # print()

    filled_trench = fill_trench(trench_locs, min_row, min_col, max_row, max_col)
    total_filled = 0

    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if (i,j) in filled_trench:
                # print('#', end='')
                total_filled += 1
            else:
                # print('.', end='')
                pass
        # print()

    print('Part 1 solution is: ' + str(total_filled))