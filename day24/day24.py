# File for day 24 of AoC 2023
# Written by Joshua Yeaton on 1/3/2024

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




if __name__ == '__main__':
    file_name = 'data.txt'
    test_dim = [200000000000000, 400000000000000]
    # file_name = 'data-test.txt'
    # test_dim = [7, 27]
    

    hailstone_data = parse_input(file_name)

    eqns_pt_1 = find_hail_eqn_pt_1(hailstone_data)

    ans_pt_1 = check_intersections(eqns_pt_1, test_dim, test_dim, hailstone_data)

    print(ans_pt_1)