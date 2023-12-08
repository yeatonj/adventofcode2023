# File for day 5 of AoC 2023
# Written by Joshua Yeaton on 12/8/2023

def parse_lines(f_in, array_in):
    f.readline()
    cur_line = f_in.readline().strip()
    while(cur_line != ''):
        cur_line = cur_line.split()
        array_in.append((int(cur_line[0]), int(cur_line[1]), int(cur_line[2])))
        cur_line = f_in.readline().strip()

def find_out_from_in(cur_val, map_array):
    for mapping in map_array:
        if ((cur_val >= mapping[1]) and (cur_val < (mapping[1] + mapping[2]))):
            return cur_val - mapping[1] + mapping[0]
    # if we get to this point, it is a direct mapping
    return cur_val

def check_in_seeds_pt2(seed_num, seed_arr, seed_arr_len):
    i = 0
    while (i < seed_arr_len):
        if ((seed_num >= seed_arr[i]) and (seed_num < (seed_arr[i] + seed_arr[i+1]))):
            return True
        i += 2
    return False

def find_in_from_out(cur_val, map_array):
    for mapping in map_array:
        if ((cur_val >= mapping[0]) and (cur_val < (mapping[0] + mapping[2]))):
            return cur_val - mapping[0] + mapping[1]
    # if we get to this point, it is a direct mapping
    return cur_val


file_name = 'data.txt'
# file_name = 'data-test.txt'

f = open(file_name)

seeds = []
seed_soil = []
soil_fert = []
fert_wat = []
wat_lgt = []
lgt_temp = []
temp_hum = []
hum_loc = []

# parse the seeds, part 1
seed_line = f.readline().strip().split()
for i in range(1,len(seed_line)):
    seeds.append(int(seed_line[i]))

# Parse seed to soil
f.readline()
parse_lines(f, seed_soil)
parse_lines(f, soil_fert)
parse_lines(f, fert_wat)
parse_lines(f, wat_lgt)
parse_lines(f, lgt_temp)
parse_lines(f, temp_hum)
parse_lines(f, hum_loc)

# At this point, all data is successfully parsed, so work through the seeds
lowest_loc = -1
for seed in seeds:
    soil = find_out_from_in(seed, seed_soil)
    fert = find_out_from_in(soil, soil_fert)
    wat = find_out_from_in(fert, fert_wat)
    lgt = find_out_from_in(wat, wat_lgt)
    temp = find_out_from_in(lgt, lgt_temp)
    hum = find_out_from_in(temp, temp_hum)
    loc = find_out_from_in(hum, hum_loc)
    if ((lowest_loc == -1) or (loc < lowest_loc)):
        lowest_loc = loc

print('Lowest location (part 1 solution) is: ' + str(lowest_loc))

# For part 2, do the same thing, but in reverse, checking to see if the seed is in the range of seeds
# first, find the minimum seed value

seed_arr_len = len(seeds)
loc = 0
found_loc = False
while (not found_loc):
    hum = find_in_from_out(loc, hum_loc)
    temp = find_in_from_out(hum, temp_hum)
    lgt = find_in_from_out(temp, lgt_temp)
    wat = find_in_from_out(lgt, wat_lgt)
    fert = find_in_from_out(wat, fert_wat)
    soil = find_in_from_out(fert, soil_fert)
    seed = find_in_from_out(soil, seed_soil)
    found_loc = check_in_seeds_pt2(seed, seeds, seed_arr_len)
    loc += 1
    if (loc % 1000 == 0):
        print('Finished checking loc: ' + str(loc))

print('Lowest location (part 2 solution) is: ' + str(loc - 1))

f.close()