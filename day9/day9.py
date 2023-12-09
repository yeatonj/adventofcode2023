# File for day 9 of AoC 2023
# Written by Joshua Yeaton on 12/9/2023

import numpy as np

file_name = 'data.txt'
# file_name = 'data-test.txt'

f = open(file_name)

rolling_sum_fwd = 0
rolling_sum_bwd = 0

for line in f:
    # First, step down through each 
    line = line.strip().split()
    np_line = np.array(line, dtype=int)
    steps = [np_line]
    while(np_line.sum() != 0):
        np_line = (np_line - np.roll(np_line,1))[1:]
        steps.append(np_line)
    # now step back through and find the number
    val_below_fwd = 0
    val_below_bwd = 0
    for i in range(len(steps)):
        val_below_fwd = steps[len(steps) - i - 1][-1] + val_below_fwd
        val_below_bwd = steps[len(steps) - i - 1][0] - val_below_bwd
    rolling_sum_fwd += val_below_fwd
    rolling_sum_bwd += val_below_bwd

print('Part 1 solution: ' + str(rolling_sum_fwd))
print('Part 2 solution: ' + str(rolling_sum_bwd))


f.close()