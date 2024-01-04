# File for day 21 of AoC 2023
# Written by Joshua Yeaton on 1/3/2024

def parse_input(file_name):
    f = open(file_name)
    coord_dic = {}
    r = 0
    for line in f:
        line = line.strip()
        c = 0
        for char in line:
            coord_dic.update({(r,c):char})
            if char == 'S':
                start_r = r
                start_c = c
            c += 1
        r += 1
    f.close()
    return (coord_dic, r, c, start_r, start_c)

def visit_adj(coord_dic, to_visit, cur_r, cur_c, max_r, max_c):
    nodes = []
    # up node
    nodes.append((cur_r - 1, cur_c))
    # down node
    nodes.append((cur_r + 1, cur_c))
    # left node
    nodes.append((cur_r, cur_c -1))
    # right node
    nodes.append((cur_r, cur_c + 1))
    for node in nodes:
        temp_node = (node[0] % max_r, node[1] % max_c)
        if coord_dic.get(temp_node) != '#' and node not in to_visit:
            to_visit.update({node:0})


if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    (coord_dic, max_r, max_c, start_r, start_c) = parse_input(file_name)

    # input starts in the direct center, with each line having no blockages - allows us to determine formula
    steps = 64 # part 1 solution
    # steps = 65 # result is 3849
    # steps = 65 + 131 # result is 34331
    # steps = 65 + 131*2 # result is 95175
    to_visit = {(start_r, start_c):0}
    for i in range(steps):
        next = {}
        for node in to_visit:
            visit_adj(coord_dic, next, node[0], node[1], max_r, max_c)
        to_visit = next

    print(len(to_visit))

    # equation is a*x^2 + b*x + c = d
    # x is steps, d is result - solved using system of equations solver
    a = 15181/17161
    b = 30901/17161
    c = -95601/17161

    final_steps = 26501365

    soln = a*final_steps**2 + b * final_steps + c
    print(round(soln))
    