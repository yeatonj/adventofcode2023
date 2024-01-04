# File for day 23 of AoC 2023
# Written by Joshua Yeaton on 1/3/2024

def parse_input(file_name):
    map_blocks = {}

    f = open(file_name)
    r = 0
    for line in f:
        c = 0
        line = line.strip()
        for char in line:
            map_blocks.update({(r,c):char})
            c += 1
        r += 1

    f.close()

    return (map_blocks, r, c)

def rec_find_longest_path(map_blocks, rows, cols, cur, goal, visited):
    # Base case, current node is goal. Return 0
    if cur == goal:
        return 0
    # Check current node. If in visited or # or oob, return -1
    if cur in visited:
        return -1
    elif cur[0] < 0 or cur[1] < 0 or cur[0] == rows or cur[1] == cols:
        return -1
    cur_node = map_blocks.get(cur)
    if cur_node == '#':
        return -1
    # at this point, we know that we are visiting this node
    visited.update({cur:1})
    # Check current node, if v of some direction, add 1 to path and visit next
    if cur_node in '<v>^':
        if cur_node == '<':
            new_node = (cur[0], cur[1] - 1)
            next_len = rec_find_longest_path(map_blocks, rows, cols, new_node, goal, visited)
        elif cur_node == 'v':
            new_node = (cur[0] + 1, cur[1])
            next_len = rec_find_longest_path(map_blocks, rows, cols, new_node, goal, visited)
        elif cur_node == '>':
            new_node = (cur[0], cur[1] + 1)
            next_len = rec_find_longest_path(map_blocks, rows, cols, new_node, goal, visited)
        else:
            new_node = (cur[0] - 1, cur[1])
            next_len = rec_find_longest_path(map_blocks, rows, cols, new_node, goal, visited)
        # unvisit this node before returning
        visited.pop(cur)
        if next_len == -1:
            return -1
        else:
            return 1 + next_len
    # Otherwise, try to visit each node:
    following_path = -1
    # visit all nodes
    new_nodes = [(cur[0], cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0], cur[1] + 1), (cur[0] - 1, cur[1])]
    for node in new_nodes:
        temp_path = rec_find_longest_path(map_blocks, rows, cols, node, goal, visited)
        if temp_path > following_path:
            following_path = temp_path
    # unvisit this node before returning
    visited.pop(cur)
    if following_path == -1:
        return -1
    else:
        return 1 + following_path

def find_longest_path(map_blocks, rows, cols, start, goal):
    # keep track of visited nodes in a dictionary
    visited_nodes = {}
    path = rec_find_longest_path(map_blocks, rows, cols, start, goal, visited_nodes)
    return path

if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    (map_blocks, max_rows, max_cols) = parse_input(file_name)

    start = (0, 1)
    goal = (max_rows - 1, max_cols -2)

    ans = find_longest_path(map_blocks, max_rows, max_cols, start, goal)

    print(ans)