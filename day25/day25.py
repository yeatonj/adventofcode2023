# File for day 25 of AoC 2023
# Written by Joshua Yeaton on 1/5/2024

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

if __name__ == '__main__':
    file_name = 'data.txt'
    file_name = 'data-test.txt'

    wire_graph = parse_input(file_name)
    print(len(wire_graph))