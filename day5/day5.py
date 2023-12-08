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

# parse the seeds
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



f.close()