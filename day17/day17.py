# File for day 17 of AoC 2023
# Written by Joshua Yeaton on 12/18/2023

import queue

def check_loc(loc, num_rows, num_cols):
    row = loc[0]
    col = loc[1]
    if (row < 0 or
        row >= num_rows or
        col < 0 or col >= num_cols):
        return False
    return True

def h_func(cur_loc, max_row, max_col):
    return ((max_row - cur_loc[0]) + (max_col - cur_loc[1]))

def create_path(came_from, cur):
    path = [cur]
    path.append(cur)
    temp_node = cur
    while (temp_node in came_from):
        prev = came_from.get(temp_node)
        path = [prev] + path
        temp_node = prev
    return path

# Checks if all nodes are in a line (same direction)
def in_line(cur_node, prev_nodes):
    rows_same = True
    cols_same = True
    for node in prev_nodes:
        if cur_node[0] != node[0]:
            rows_same = False
        if cur_node[1] != node[1]:
            cols_same = False
    return rows_same or cols_same

# finds current direction
def find_dir(cur_node, prev_node):
    # !!
    row_change = cur_node[0] - prev_node[0]
    col_change = cur_node[1] - prev_node[1]
    if row_change == 0:
        if col_change > 0:
            return '>'
        else:
            return '<'
    else:
        if row_change > 0:
            return 'v'
        else:
            return '^'

# Do a-star, but store prev directions in addition to current node in order to properly calculate directions
# Make 'came from' contain 2 prev nodes instead of just one
def a_star(start, goal, loss_map, max_row, max_col):
    # discovered nodes that we will iterate through
    open_points = queue.PriorityQueue()
    # tracks preceding nodes (the previous 2, if applicable)
    came_from = {}
    # cost of cheapest path from start to given node that we know of
    g_score = {}
    # gscore + h = fscore
    f_score = {}
    for pt in loss_map:
        g_score.update({pt:'inf'})
        f_score.update({pt:'inf'})
    g_score.update({start:0})
    f_score.update({start:h_func(start, max_row, max_col)})
    # add start to open_points
    open_points.put([f_score.get(start), start])
    
    while (not open_points.empty()):
        cur = open_points.get()
        print(cur)
        cur_node = cur[1]
        cur_row = cur_node[0]
        cur_col = cur_node[1]
        if cur_node == goal:
            return create_path(came_from, cur_node)
        neighbors = []
        prev_nodes = []
        temp_node = cur_node
        # Get previous nodes
        while (len(prev_nodes) < 3 and temp_node in came_from):
            prev_nodes.append(came_from.get(temp_node))
            temp_node = prev_nodes[-1]
        if (len(prev_nodes) == 0):
            # Starting location, bottom and right are adj !!
            neighbors.append((cur_node[0] + 1,cur_node[1]))
            neighbors.append((cur_node[0],cur_node[1] + 1))
        else:
            # up
            neighbors.append((cur_row - 1, cur_col))
            # right
            neighbors.append((cur_row, cur_col + 1))
            # down
            neighbors.append((cur_row + 1, cur_col))
            # left
            neighbors.append((cur_row, cur_col - 1))
            cur_dir = find_dir(cur_node, prev_nodes[0])
            if (len(prev_nodes) < 3 or not in_line(cur_node, prev_nodes)):
                # all 3 nodes are neighbors, remove one opposite direction of travel
                if cur_dir == '^':
                    del neighbors[2]
                elif cur_dir == '>':
                    del neighbors[3]
                elif cur_dir == 'v':
                    del neighbors[0]
                else: # cur_dir == '<'
                    del neighbors[1]
            else:
                # only left and right nodes are neighbors
                if cur_dir == '^':
                    del neighbors[2]
                    del neighbors[0]
                elif cur_dir == '>':
                    del neighbors[3]
                    del neighbors[1]
                elif cur_dir == 'v':
                    del neighbors[2]
                    del neighbors[0]
                else: # cur_dir == '<'
                    del neighbors[3]
                    del neighbors[1]
        print(neighbors)
        print(prev_nodes)
        for neighbor in neighbors:
            # first, check that neighbor is valid
            if not check_loc(neighbor, max_row, max_col):
                continue
            dist = loss_map.get(neighbor)
            est_g_score = g_score.get(cur_node) + dist
            neighbor_g_score = g_score.get(neighbor)
            if ((neighbor_g_score == 'inf') or (est_g_score < neighbor_g_score)):
                print(neighbor)
                came_from.update({neighbor:cur_node})
                g_score.update({neighbor:est_g_score})
                f_score.update({neighbor:(est_g_score + h_func(neighbor, max_row, max_col))})
                if (not any(neighbor) in loc for loc in open_points.queue):
                    open_points.put([f_score.get(neighbor), neighbor]) 
    # if we get here, we have failed to find a path
    return -1

if __name__ == '__main__':
    file_name = 'data.txt'
    file_name = 'data-test.txt'
    file_name = 'data-test-2.txt'

    f = open(file_name)

    loss_map = {}
    row = 0
    for line in f:
        line = line.strip()
        col= 0
        for c in line:
            loss_map.update({(row, col):int(c)})
            col += 1
        row += 1
    rows = row
    cols = col

    start = (0,0)
    goal = (rows - 1, cols - 1)
    path = a_star(start, goal, loss_map, rows, cols)

    print('Part 1 solution is: ' + str(len(path)))

    total = 0

    for i in range(rows):
        for j in range(col):
            if (i,j) in path:
                print('#', end='')
                total += loss_map.get((i,j))
            else:
                print('.', end='')
        print()

    total -= loss_map.get((0,0))
    print(total)

    # Answer of 1008 is too high.

    f.close()