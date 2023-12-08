# File for day 8 of AoC 2023
# Written by Joshua Yeaton on 12/8/2023

import math

file_name = 'data.txt'
# file_name = 'data-test-1.txt'
# file_name = 'data-test-2.txt'
# file_name = 'data-test-3.txt'

f = open(file_name)

directions = f.readline()
directions = directions.strip()

# skip the next line
f.readline()

maze_dict = {}
start_nodes = set()
# Parse the maze (including, for pt2, grabbing all the nodes that end in A)
for line in f:
    line = line.strip()
    node = line[0:3]
    if node[-1] == 'A':
        start_nodes.update([node])
    left = line[7:10]
    right = line[12:15]
    node_dirs = {}
    node_dirs.update({'R':right})
    node_dirs.update({'L':left})
    maze_dict.update({node:node_dirs})

# Now, journey through the maze until we reach ZZZ
cur_node = 'AAA'
cur_dir_index = 0
dir_len = len(directions)

# # uncomment for part 1
# while(cur_node != 'ZZZ'):
#     cur_dir = directions[cur_dir_index % dir_len]
#     cur_node = maze_dict.get(cur_node).get(cur_dir)
#     cur_dir_index +=1
# print('Number of steps, part 1: ' + str(cur_dir_index))

# Part 2
encounter_z = []
for start_node in start_nodes:
    cur_node = start_node
    cur_dir_index = 0
    while(cur_node[-1] != 'Z'):
        cur_dir = directions[cur_dir_index % dir_len]
        cur_node = maze_dict.get(cur_node).get(cur_dir)
        cur_dir_index +=1
    encounter_z.append(cur_dir_index)
# print(encounter_z)
# Now, find their LCM and use that as the answer

print('Number of steps, part 2: ' + str(math.lcm(*encounter_z)))


f.close()