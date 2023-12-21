# File for day 18 of AoC 2023
# Written by Joshua Yeaton on 12/18/2023

import queue

def parse_line(line):
    line = line.strip()
    split_line = line.split()
    return (split_line[0], int(split_line[1]), split_line[2])

def parse_line_pt_2(line):
    line = line.strip()
    split_line = line.split()
    instr = split_line[2].strip('()')
    dir_num = instr[-1]
    hex_num = instr[1:-1]
    hex_num = '0x' + hex_num
    if dir_num == '0':
        dir = 'R'
    elif dir_num == '1':
        dir = 'D'
    elif dir_num == '2':
        dir = 'L'
    elif dir_num == '3':
        dir = 'U'
    return (dir, int(hex_num, 0))

def add_point(cur_loc, dir, dist, all_points, boundary_count):
    if dir == 'R':
        delta = (0, 1*dist)
    elif dir == 'L':
        delta = (0,-1*dist)
    elif dir == 'U':
        delta = (-1*dist, 0)
    elif dir == 'D':
        delta = (1*dist, 0)
    new_loc = (cur_loc[0] + delta[0], cur_loc[1] + delta[1])
    all_points.append(new_loc)
    boundary_count[0] += dist
    return new_loc

def shoelace_area(points):
    cur_loc = points[0]
    total = 0
    for i in range(1,len(points)):
        new_loc = points[i]
        total += ((cur_loc[0] + new_loc[0])*(cur_loc[1] - new_loc[1]))
        cur_loc = new_loc
    total /= 2
    return total

def pick_thm(shoe_area, boundary_count):
    interior_pts = shoe_area - boundary_count/2 + 1
    return int(interior_pts)

if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    f = open(file_name)

    trench_locs = {}
    cur_loc = (0,0)
    trench_locs.update({cur_loc:1})
    all_points =[cur_loc]
    boundary_count = [0]

    for line in f:
        # (dir, dist, color) = parse_line(line)
        (dir, dist) = parse_line_pt_2(line)
        # cur_loc = add_trench(cur_loc, dir, dist, trench_locs)
        cur_loc = add_point(cur_loc, dir, dist, all_points, boundary_count)

    shoe_area = shoelace_area(all_points)

    interior_pts = pick_thm(shoe_area, boundary_count[0])

    print('Answer is: '+ str(interior_pts + boundary_count[0]))
    

    f.close()