# File for day 23 of AoC 2023
# Written by Joshua Yeaton on 1/3/2024

import copy

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

def get_dist_to_next_node(node, dir, intersections, map_blocks):
    visited = {node:1}
    cur_node = node
    if dir =='^':
        next_node = (cur_node[0] - 1, cur_node[1])
    elif dir == 'v':
        next_node = (cur_node[0] + 1, cur_node[1])
    elif dir == '<':
        next_node = (cur_node[0], cur_node[1] - 1)
    else:
        next_node = (cur_node[0], cur_node[1] + 1)
    path_len = 1
    while (next_node not in intersections):
        cur_node = next_node
        visited.update({cur_node:1})
        path_len += 1
        adj_nodes = [(cur_node[0] - 1, cur_node[1]), (cur_node[0] + 1, cur_node[1]), (cur_node[0], cur_node[1] - 1), (cur_node[0], cur_node[1] + 1)]
        for poss_node in adj_nodes:
            if poss_node in visited:
                continue
            node_type = map_blocks.get(poss_node)
            if node_type != '#':
                next_node = poss_node
                break
    return (next_node, path_len)


def reduce_graph(map_blocks, start, goal, rows, cols):
    intersections = {}
    for r in range(1, rows -1):
        for c in range(1, cols - 1):
            adj_paths = check_adj_paths((r,c), map_blocks)
            if len(adj_paths) > 2:
                intersections.update({(r,c):adj_paths})

    intersections.update({start:{'v':1}})
    intersections.update({goal:{'^':1}})
    reduced_graph = {}
    for node in intersections:
        exits = intersections.get(node)
        temp_dic = {}
        for dir in exits:
            (dest_dist, dest_node) = get_dist_to_next_node(node, dir, intersections, map_blocks)
            temp_dic.update({dir:(dest_dist, dest_node)})
        reduced_graph.update({node:temp_dic})
    return reduced_graph

# does not need to check for edge cases
def check_adj_paths(node, map_blocks):
    # make sure we are on a path
    if map_blocks.get(node) == '#':
        return {}
    # Otherwise, return the actual adjacent paths
    adj_paths = {}
    up_node = (node[0] - 1, node[1])
    dn_node = (node[0] + 1, node[1])
    le_node = (node[0], node[1] - 1)
    ri_node = (node[0], node[1] + 1)
    if map_blocks.get(up_node) != '#':
        adj_paths.update({'^':1})
    if map_blocks.get(dn_node) != '#':
        adj_paths.update({'v':1})
    if map_blocks.get(le_node) != '#':
        adj_paths.update({'<':1})
    if map_blocks.get(ri_node) != '#':
        adj_paths.update({'>':1})
    return adj_paths


def find_longest_path(map_blocks, rows, cols, start, goal):
    cur_max_len = -1
    cur_paths = []
    # structure is (cur_coord, cur_len, {visited_nodes_on_path})
    cur_paths.append((start, 0, {}))
    while(len(cur_paths) != 0):
        cur_path = cur_paths.pop(-1)
        cur_coord = cur_path[0]
        cur_len = cur_path[1]
        visited = cur_path[2]
        if cur_coord == goal and cur_len > cur_max_len:
            cur_max_len = cur_len
            print(cur_len)
            continue
        # Check current node. If in visited or # or oob, ignore
        if cur_coord in visited:
            continue
        elif cur_coord[0] < 0 or cur_coord[1] < 0 or cur_coord[0] == rows or cur_coord[1] == cols:
            continue
        cur_node = map_blocks.get(cur_coord)
        if cur_node == '#':
            continue

        # commented out for pt2
        # Check current node, if v of some direction, add to paths to check
        if cur_node in '<v>^':
            if cur_node == '<':
                new_node = (cur_coord[0], cur_coord[1] - 1)
            elif cur_node == 'v':
                new_node = (cur_coord[0] + 1, cur_coord[1])
            elif cur_node == '>':
                new_node = (cur_coord[0], cur_coord[1] + 1)
            else:
                new_node = (cur_coord[0] - 1, cur_coord[1])
            new_visited = copy.deepcopy(visited)
            new_visited.update({cur_coord:1})
            new_path = (new_node, cur_len + 1, new_visited)
            cur_paths.append(new_path)
            continue
    
        # Otherwise, try to visit each node:
        # visit all nodes
        new_nodes = [(cur_coord[0], cur_coord[1] - 1), (cur_coord[0] + 1, cur_coord[1]), (cur_coord[0], cur_coord[1] + 1), (cur_coord[0] - 1, cur_coord[1])]
        for new_node in new_nodes:
            new_visited = copy.deepcopy(visited)
            new_visited.update({cur_coord:1})
            new_path = (new_node, cur_len + 1, new_visited)
            cur_paths.append(new_path)

    # Now, simply return our longest path
    return cur_max_len


def find_longest_path_reduced(reduced_graph, start, goal):
    skips = 0
    cur_max_len = -1
    # first, find the best hope
    poss_path_lengths = []
    max_nodes_seen = len(reduced_graph) - 1
    for inter in reduced_graph:
        for dir in reduced_graph.get(inter):
            poss_path_lengths.append(reduced_graph.get(inter).get(dir)[1])
    poss_path_lengths.sort(reverse=True)
    best_hope = sum(poss_path_lengths)
    cur_paths = []
    # structure is (cur_coord, cur_len, {visited_nodes_on_path}, best_hope, prev_path)
    cur_paths.append((start, 0, {}, best_hope, 0))
    while(len(cur_paths) != 0):
        cur_path = cur_paths.pop(-1)
        cur_coord = cur_path[0]
        cur_len = cur_path[1]
        visited = cur_path[2]
        cur_best_hope = cur_path[3]
        prev_path = cur_path[4]
        if cur_coord == goal and cur_len > cur_max_len:
            cur_max_len = cur_len
            print(cur_max_len)
            continue
        # Check current node. If in visited, ignore
        if cur_coord in visited:
            continue
        # if our current best possible is less than our current best, move on
        if cur_best_hope < cur_max_len:
            skips += 1
            continue
    
        # Try to visit each node adjacent to this one:
        adj_nodes = []
        adj_dirs = reduced_graph.get(cur_coord)
        adj_edges = 0
        for dir in adj_dirs:
            adj_node = adj_dirs.get(dir)
            adj_edges += adj_node[1]
            # if we are at the intersection before exit, only one possible path
            if cur_coord == (137,127) and dir != 'v':
                continue
            adj_nodes.append(adj_node)
        new_best_hope = cur_best_hope - adj_edges + prev_path
        for new_node in adj_nodes:
            new_node_coord = new_node[0]
            new_node_dist = new_node[1]
            new_visited = copy.deepcopy(visited)
            new_visited.update({cur_coord:1})
            new_path = (new_node_coord, cur_len + new_node_dist, new_visited, new_best_hope, new_node_dist)
            cur_paths.append(new_path)
    # Now, simply return our longest path
    return cur_max_len


if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    (map_blocks, max_rows, max_cols) = parse_input(file_name)

    start = (0, 1)
    goal = (max_rows - 1, max_cols -2)

    # ans = find_longest_path(map_blocks, max_rows, max_cols, start, goal)

    reduced_graph = reduce_graph(map_blocks, start, goal, max_rows, max_cols)
    # we now have a reduced graph - explore it!
    ans = find_longest_path_reduced(reduced_graph, start, goal)
    print(ans)
    # 6486 is too low
    # 6522 is too low
    # 6558 is too low
    # solved with 6586
    # print(ans)