# File for day 24 of AoC 2023
# Written by Joshua Yeaton on 1/3/2024

import numpy

# hailstone data is an array with entries [([pos0], [vel0]), ..., ([posn], [veln])]
def parse_input(file_name):
    f = open(file_name)
    hailstone_data = []
    for line in f:
        line = line.strip()
        pos_vel = line.split('@')
        pos = pos_vel[0].split(',')
        vel = pos_vel[1].split(',')
        pos_int = [0, 0, 0]
        vel_int = [0, 0, 0]
        for i in range(3):
            pos_int[i] = int(pos[i].strip())
            vel_int[i] = int(vel[i].strip())
        hailstone_data.append((pos_int, vel_int))
    f.close()
    return hailstone_data

def find_hail_eqn_pt_1(hailstone_data):
    eqns = []
    for stone in hailstone_data:
        m = stone[1][1] / stone[1][0]
        b = stone[0][1] - stone[0][0]*m
        eqns.append((m, b))
    return eqns

def check_intersections(eqns, dim_x, dim_y, hailstone_data):
    collisions = 0
    for i in range(len(eqns)):
        for j in range(i, len(eqns)):
            if check_intersection(eqns[i], eqns[j], dim_x, dim_y, hailstone_data[i][0][0], hailstone_data[i][1][0], hailstone_data[j][0][0], hailstone_data[j][1][0]):
                collisions += 1
    return collisions

def check_intersection(eq1, eq2, dim_x, dim_y, init_x_pos1, x_vel1, init_x_pos2, x_vel2):
    a = eq1[0]
    b = eq2[0]
    c = eq1[1]
    d = eq2[1]
    if a - b == 0:
        return False
    x_int = (d - c) / (a - b)
    y_int = a*x_int + c
    if (x_int > dim_x[0] and x_int < dim_x[1] and y_int > dim_y[0] and y_int < dim_y[1]):
        cond1 = (init_x_pos1 < x_int and x_vel1 > 0) or (init_x_pos1 > x_int and x_vel1 < 0)
        cond2 = (init_x_pos2 < x_int and x_vel2 > 0) or (init_x_pos2 > x_int and x_vel2 < 0)
        if cond1 and cond2:
            return True
    return False

def solve_pt_2(hailstone_data):
    # pick 3 hailstones
    stone_1 = hailstone_data[0]
    stone_2 = hailstone_data[1]
    stone_3 = hailstone_data[2]

    x0 = stone_1[0][0]
    x1 = stone_2[0][0]
    x2 = stone_3[0][0]

    y0 = stone_1[0][1]
    y1 = stone_2[0][1]
    y2 = stone_3[0][1]

    z0 = stone_1[0][2]
    z1 = stone_2[0][2]
    z2 = stone_3[0][2]

    dx0 = stone_1[1][0]
    dx1 = stone_2[1][0]
    dx2 = stone_3[1][0]

    dy0 = stone_1[1][1]
    dy1 = stone_2[1][1]
    dy2 = stone_3[1][1]

    dz0 = stone_1[1][2]
    dz1 = stone_2[1][2]
    dz2 = stone_3[1][2]

    # we need a 6 x 6 matrix with appropriate coeff
    # use vector [X, Y, Z, dX, dY, dZ]
    a = numpy.zeros((6, 6))
    b = numpy.zeros(6)
    # eqn 1
    a[0][0] = dy1 - dy0
    a[0][1] = dx0 - dx1
    a[0][2] = 0
    a[0][3] = y0 - y1
    a[0][4] = x1 - x0
    a[0][5] = 0
    b[0] = x1*dy1 - y1*dx1 - x0*dy0 + y0*dx0
    # eqn 2
    a[1][0] = dz1 - dz0
    a[1][1] = 0
    a[1][2] = dx0 - dx1
    a[1][3] = z0 -z1
    a[1][4] = 0
    a[1][5] = x1 - x0
    b[1] = x1*dz1 - z1*dx1 - x0*dz0 +z0*dx0
    # eqn 3
    a[2][0] = 0
    a[2][1] = dz0 - dz1
    a[2][2] = dy1 - dy0
    a[2][3] = 0
    a[2][4] = z1 - z0
    a[2][5] = y0 - y1
    b[2] = z1*dy1 - y1*dz1 - z0*dy0 + y0*dz0
    # eqn 4
    a[3][0] = dy2 - dy0
    a[3][1] = dx0 - dx2
    a[3][2] = 0
    a[3][3] = y0 - y2
    a[3][4] = x2 - x0
    a[3][5] = 0
    b[3] = x2*dy2 - y2*dx2 - x0*dy0 + y0*dx0
    # eqn 5
    a[4][0] = dz2 - dz0
    a[4][1] = 0
    a[4][2] = dx0 - dx2
    a[4][3] = z0 -z2
    a[4][4] = 0
    a[4][5] = x2 - x0
    b[4] = x2*dz2 - z2*dx2 - x0*dz0 +z0*dx0
    # eqn 6
    a[5][0] = 0
    a[5][1] = dz0 - dz2
    a[5][2] = dy2 - dy0
    a[5][3] = 0
    a[5][4] = z2 - z0
    a[5][5] = y0 - y2
    b[5] = z2*dy2 - y2*dz2 - z0*dy0 + y0*dz0
    
    soln = numpy.linalg.solve(a,b)
    return sum(soln[0:3])



if __name__ == '__main__':
    file_name = 'data.txt'
    test_dim = [200000000000000, 400000000000000]
    # file_name = 'data-test.txt'
    # test_dim = [7, 27]
    

    hailstone_data = parse_input(file_name)

    eqns_pt_1 = find_hail_eqn_pt_1(hailstone_data)

    ans_pt_1 = check_intersections(eqns_pt_1, test_dim, test_dim, hailstone_data)

    ans_pt_2 = solve_pt_2(hailstone_data)

    print(ans_pt_1)
    print(ans_pt_2)