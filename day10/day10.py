# File for day 10 of AoC 2023
# Written by Joshua Yeaton on 12/10/2023

import queue

# Function to add a pipe to a 3x representation of it
def add_node_full(node, pipe_t, full_map):
    # First, add all blank sections to it
    row = 3*node[0]
    col = 3*node[1]
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            full_map.update({(r,c):'.'})
    # empty square
    if pipe_t == '.':
        pass
    elif pipe_t == '|':
        #vertical
        full_map.update({(row, col + 1):'P'})
        full_map.update({(row + 1, col + 1):'P'})
        full_map.update({(row + 2, col + 1):'P'})
    elif pipe_t == '-':
        #horizontal
        full_map.update({(row + 1, col):'P'})
        full_map.update({(row + 1, col + 1):'P'})
        full_map.update({(row + 1, col + 2):'P'})
    elif pipe_t == 'L':
        #down right
        full_map.update({(row, col + 1):'P'})
        full_map.update({(row + 1, col + 1):'P'})
        full_map.update({(row + 1, col + 2):'P'})
    elif pipe_t == 'J':
        #down left
        full_map.update({(row, col + 1):'P'})
        full_map.update({(row + 1, col + 1):'P'})
        full_map.update({(row + 1, col):'P'})
    elif pipe_t == '7':
        #up left
        full_map.update({(row + 1, col):'P'})
        full_map.update({(row + 1, col + 1):'P'})
        full_map.update({(row + 2, col + 1):'P'})
    elif pipe_t == 'F':
        #up right !!
        full_map.update({(row + 1, col + 2):'P'})
        full_map.update({(row + 1, col + 1):'P'})
        full_map.update({(row + 2, col + 1):'P'})
    return

# Function to find all adjacent nodes
def find_adj(node, max_row, max_col):
    adj_nodes = []
    # Find left node
    if node[1] > 0:
        adj_nodes.append((node[0], node[1] - 1))
    # Find right node
    if node[1] < max_col:
        adj_nodes.append((node[0], node[1] + 1))
    # Find up node
    if node[0] > 0:
        adj_nodes.append((node[0] - 1, node[1]))
    # Find down node
    if node[0] < max_row:
        adj_nodes.append((node[0] + 1, node[1]))
    return adj_nodes



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
max_mode = (-1, -1)

for node in node_dists:
    dist = node_dists.get(node)
    if  dist > max_node_dist:
        max_node = node
        max_node_dist = dist


print('Maximum distance (part 1) is: ' + str(max_node_dist))

# Now, get the actual tiles in the loop. We will convert all others to dots.
in_loop = {}

loop_nodes = queue.SimpleQueue()
loop_nodes.put(max_node)
while (not loop_nodes.empty()):
    cur_node = loop_nodes.get()
    cur_dist = node_dists.get(cur_node)
    in_loop.update({cur_node:cur_dist})
    adj_nodes = find_adj(cur_node, max_row + 1, max_col + 1)
    for adj_node in adj_nodes:
        if adj_node in node_dists:
            if (node_dists.get(adj_node) == (cur_dist -1)):
                loop_nodes.put(adj_node)


# At this point, we have everything that's actually in the loop included, and nothing else.
# First, update the actual starting node with the correct pipe
# !! note this is specific to my puzzle
nodes.update({start_node:'L'}) # Actual data
# nodes.update({start_node:'7'}) # Test data

full_map = {} # 3x map of the whole pipe structure
# update to the 3x structure
for i in range(max_row + 1):
    for j in range(max_col + 1):
        if (i,j) in in_loop:
            add_node_full((i,j), nodes.get((i,j)), full_map)
        else:
            add_node_full((i,j), '.', full_map)

# Now, start at (0,0) and fill in everything that is outside
to_check = queue.SimpleQueue()
to_check.put((0,0))
checked = {}
while(not to_check.empty()):
    cur = to_check.get()
    left = (cur[0], cur[1] - 1)
    if left in full_map and left not in checked:
        checked.update({left:0})
        status = full_map.get(left)
        if status == '.':
            full_map.update({left:'O'})
            to_check.put(left)

    right = (cur[0], cur[1] + 1)
    if right in full_map and right not in checked:
        checked.update({right:0})
        status = full_map.get(right)
        if status == '.':
            full_map.update({right:'O'})
            to_check.put(right)

    up = (cur[0] - 1, cur[1])
    if up in full_map and up not in checked:
        checked.update({up:0})
        status = full_map.get(up)
        if status == '.':
            full_map.update({up:'O'})
            to_check.put(up)

    down = (cur[0] + 1, cur[1])
    if down in full_map and down not in checked:
        checked.update({down:0})
        status = full_map.get(down)
        if status == '.':
            full_map.update({down:'O'})
            to_check.put(down)

inside_pipes = 0

# Now, loop through each of the actual elements. each of its 4 corners must be '.' to be inside
for i in range(max_row + 1):
    for j in range(max_col + 1):
        top_left = (3*i, 3*j)
        top_right = (3*i, 3*j + 2)
        bot_left = (3*i + 2, 3*j)
        bot_right = (3*i + 2, 3*j + 2)
        if (full_map.get(top_left) == '.' and 
            full_map.get(top_right) == '.' and 
            full_map.get(bot_left) == '.' and
            full_map.get(bot_right) == '.'):
            inside_pipes += 1

print('Tiles inside (part 2): ' + str(inside_pipes))

# # used to print the loop, if desired
# for i in range(3*max_row + 3):
#     for j in range(3*max_col + 3):
#         print(full_map.get((i,j)), end='')
#     print()

f.close()