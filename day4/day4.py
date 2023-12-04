# File for day 4 of AoC 2023
# Written by Joshua Yeaton on 12/4/2023

f = open('data.txt')
# f = open('data-test.txt')

total_points = 0

for line in f:
    line_points = 0
    entries = line.split('|')
    # First, extract the winning numbers
    winning_nums = ''.join(entries[0])
    winning_nums = winning_nums.split(':')
    winning_nums = ''.join(winning_nums[1])
    winning_nums = winning_nums.strip()
    winning_nums = winning_nums.split(' ')

    # Then, extract the selected numbers
    selected_nums = entries[1].strip()
    selected_nums = selected_nums.split(' ')
    while ('' in selected_nums):
        selected_nums.remove('')
    
    # now calculate the points
    for guess in selected_nums:
        if ((guess in winning_nums) and (line_points == 0)):
            line_points = 1
        elif (guess in winning_nums):
            line_points *= 2
    total_points += line_points

print('Total points: ' + str(total_points))

f.close()