# File for day 25 of AoC 2023
# Written by Joshua Yeaton on 1/5/2024

import random

def parse_input(file_name):
    f = open(file_name)

    connec_graph = {}

    for line in f:
        line = line.strip()
        node = line.split(':')[0]
        connec_graph.update({node:{}})
    f.close()

    f = open(file_name)
    for line in f:
        line = line.strip()
        raw_node = line.split(':')
        node = raw_node[0]
        raw_connecs = raw_node[1].strip()
        raw_connecs = raw_connecs.split(' ')
        sub_dic = connec_graph.get(node)
        for conn_node in raw_connecs:
            sub_dic.update({conn_node:1})
            if conn_node not in connec_graph:
                connec_graph.update({conn_node:{}})
            connec_graph.get(conn_node).update({node:1})
    f.close()
    return connec_graph

# returns all edges visited by the bfs
def bfs(start, end, graph):
    traveled_edges = {}
    visited_nodes = {}
    visit_queue = [(start, None)]
    while (len(visit_queue) > 0):
        cur_edge = visit_queue.pop(-1)
        cur_node = cur_edge[0]
        prev_node = cur_edge[1]
        if cur_node in visited_nodes:
            continue
        if prev_node != None:
            traveled_edges.update({cur_edge:1})
            traveled_edges.update({(cur_edge[1], cur_edge[0]):1})
        visited_nodes.update({cur_node:1})
        # finish if we're at the end
        if cur_node == end:
            return traveled_edges
        adj_nodes = graph.get(cur_node)
        adj_nodes = list(adj_nodes.keys())
        random.shuffle(adj_nodes)
        for node in adj_nodes:
            # !! we need to pick these randomly...
            visit_queue.append((node, cur_node))


def bfs_count(start, graph):
    visited_nodes = {}
    visit_queue = [start]
    while (len(visit_queue) > 0):
        cur_node = visit_queue.pop(-1)
        if cur_node in visited_nodes:
            continue
        visited_nodes.update({cur_node:1})
        adj_nodes = graph.get(cur_node)
        for node in adj_nodes:
            visit_queue.append(node)
    return len(visited_nodes)


if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    wire_graph = parse_input(file_name)
    node_array = [node_name for node_name in wire_graph]
    num_nodes = len(node_array)
    print(num_nodes)
    
    # pick two (different) random nodes and do a BFS, adding visited nodes to a node counter at the end
    num_trials = 10000
    visited_edges = {}
    for i in range(num_trials):
        node_1 = node_array[random.randint(0, num_nodes -1)]
        node_2 = node_array[random.randint(0, num_nodes -1)]
        if node_1 == node_2:
            # just skip this trial
            continue
        trial_traveled_edges = bfs(node_1, node_2, wire_graph)
        for edge in trial_traveled_edges:
            if edge not in visited_edges:
                visited_edges.update({edge:1})
            else:
                cur_edge_count = visited_edges.get(edge)
                visited_edges.update({edge:(cur_edge_count + 1)})

    edge_array = []
    for edge in visited_edges:
        edge_count = visited_edges.get(edge)
        edge_array.append((edge_count, edge))

    edge_array.sort(reverse=True)
    count = 0
    for edge in edge_array:
        if count > 10:
            break
        count += 1

    rem_edges = [edge_array[0][1], edge_array[2][1], edge_array[4][1]]
    # remove these edges
    for rem_edge in rem_edges:
        source_node_sub_dic = wire_graph.get(rem_edge[0])
        dest_node_sub_dic = wire_graph.get(rem_edge[1])
        source_node_sub_dic.pop(rem_edge[1])
        dest_node_sub_dic.pop(rem_edge[0])



    sub_graph_size = bfs_count(node_1, wire_graph)
    print((num_nodes-sub_graph_size)*sub_graph_size)



