# File for day 10 of AoC 2023
# Written by Joshua Yeaton on 12/10/2023

import queue

# Function to check nodes adjacent to pipes
def get_adj_nodes(cur_loc, pipe_type, max_row, max_col, nodes):
    adj_nodes = []
    cur_row = cur_loc[0]
    cur_col = cur_loc[1]
    if pipe_type == '|':
        if cur_row == 0 or cur_row == max_row:
            # off the map
            return []
        up_node = (cur_row - 1, cur_col)
        down_node = (cur_row + 1, cur_col)
        up_pipe = nodes.get(up_node)
        down_pipe = nodes.get(down_node)
        if up_pipe not in 'S|7F' or down_pipe not in 'S|LJ':
            return []
        adj_nodes = [up_node, down_node]
    elif pipe_type == '-':
        if cur_col == 0 or cur_col == max_col:
            # off the map
            return []
        left_node = (cur_row, cur_col - 1)
        right_node = (cur_row, cur_col + 1)
        left_pipe = nodes.get(left_node)
        right_pipe = nodes.get(right_node)
        if left_pipe not in 'S-LF' or right_pipe not in 'S-J7':
            return []
        adj_nodes = [left_node, right_node]
    elif pipe_type == 'L':
        if cur_row == 0 or cur_col == max_col:
            # off the map
            return []
        up_node = (cur_row - 1, cur_col)
        right_node = (cur_row, cur_col + 1)
        up_pipe = nodes.get(up_node)
        right_pipe = nodes.get(right_node)
        if up_pipe not in 'S|7F' or right_pipe not in 'S-J7':
            return []
        adj_nodes = [up_node, right_node]
    elif pipe_type == 'J':
        if cur_col == 0 or cur_row == 0:
            # off the map
            return []
        left_node = (cur_row, cur_col - 1)
        up_node = (cur_row - 1, cur_col)
        left_pipe = nodes.get(left_node)
        up_pipe = nodes.get(up_node)
        if left_pipe not in 'S-LF' or up_pipe not in 'S|7F':
            return []
        adj_nodes = [left_node, up_node]
    elif pipe_type == '7':
        if cur_col == 0 or cur_row == max_row:
            # off the map
            return []
        left_node = (cur_row, cur_col - 1)
        down_node = (cur_row + 1, cur_col)
        left_pipe = nodes.get(left_node)
        down_pipe = nodes.get(down_node)
        if left_pipe not in 'S-LF' or down_pipe not in 'S|LJ':
            return []
        adj_nodes = [left_node, down_node]
    elif pipe_type == 'F':
        if cur_row == max_row or cur_col == max_col:
            # off the map
            return []
        down_node = (cur_row + 1, cur_col)
        right_node = (cur_row, cur_col + 1)
        down_pipe = nodes.get(down_node)
        right_pipe = nodes.get(right_node)
        if down_pipe not in 'S|LJ' or right_pipe not in 'S-J7':
            return []
        adj_nodes = [down_node, right_node]
    else: # 'S'
        for pipe in '|-LJ7F':
            poss_nodes = get_adj_nodes(cur_loc, pipe, max_row, max_col, nodes)
            for n in poss_nodes:
                adj_nodes.append(n)
    return adj_nodes

file_name = 'data.txt'
# file_name = 'data-test.txt'

f = open(file_name)

nodes = {}

row = 0
# Build the graph
for r in f:
    r = r.strip()
    col = 0
    for c in r:
        # find the start node
        if c == 'S':
            start_node = (row, col)
        nodes.update({(row,col):c})
        col += 1
    row += 1

max_row = row - 1
max_col = col - 1

node_dists = {}

# Now, traverse the graph
to_visit = queue.SimpleQueue()
to_visit.put(start_node)
node_dists.update({start_node:0})
# While we still have nodes to visit
i = 0
while (not to_visit.empty()):
    # Pop the current node off the to_visit queue
    cur_node = to_visit.get()
    cur_dist = node_dists.get(cur_node)

    # Get our adjacent nodes
    pipe_type = nodes.get(cur_node)
    adj_nodes = get_adj_nodes(cur_node, pipe_type, max_row, max_col, nodes)
    if (not adj_nodes):
        # continue if we don't have any nodes
        continue
    # If the adjacent nodes can be visited in a shorter distance, update the distances dict, then visit that node
    for n in adj_nodes:
        if ((n in node_dists) and (node_dists.get(n) < cur_dist + 1)):
            continue
        else:
            node_dists.update({n:(cur_dist + 1)})
            to_visit.put(n)

max_node_dist = 0
for dist in node_dists.values():
    if dist > max_node_dist:
        max_node_dist = dist

print('Maximum distance (part 1) is: ' + str(max_node_dist))
        

f.close()