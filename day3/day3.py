# File for day 3 of AoC 2023
# Written by Joshua Yeaton on 12/3/2023

def check_adj_symbols(symbol_dic, start_col, end_col, row, max_row, max_col):
    # rebuild the search area by building a rectangle around the number
    if (start_col > 0):
        start_col -= 1
    if (end_col < max_col):
        end_col += 1
    if (row > 0):
        start_row = row - 1
    else:
        start_row = row
    if (row < max_row):
        end_row = row + 1
    else:
        end_row = row

    # Check for symbols in that box
    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            if (r, c) in symbol_dic:
                return True
    return False

def check_adj_gears(gear_dic, start_col, end_col, row, max_row, max_col, num):
    # rebuild the search area by building a rectangle around the number
    if (start_col > 0):
        start_col -= 1
    if (end_col < max_col):
        end_col += 1
    if (row > 0):
        start_row = row - 1
    else:
        start_row = row
    if (row < max_row):
        end_row = row + 1
    else:
        end_row = row

    # Check for symbols in that box
    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            # Add gears to the array
            if (r, c) in gear_dic:
                # get current array in gear_dic
                cur_arr = gear_dic.get((r,c))
                # append number to array
                cur_arr.append(num)
                # re-add it
                gear_dic.update({(r,c):cur_arr})
    return
    

f_name = 'data.txt'
# f_name = 'data-test.txt'

f = open(f_name)

symbol_locs = {}
gear_locs = {}
not_symbols = '1234567890.\n'

# Find the location of all symbols
row = 0
for line in f:
    max_col = len(line)
    col = 0
    for c in line:
        if c not in not_symbols:
            symbol_locs.update({(row,col):c})
        if c == '*':
            gear_locs.update({(row,col):[]})
        col += 1
    row += 1
f.close()
max_row = row

# reopen file and find numbers, then see if they are adj to symbols
part_num_sum = 0
f = open(f_name)

row = 0
for line in f:
    col = 0
    while (col < len(line)):
        num = ''
        if line[col].isnumeric():
            start_col = col
            while(col < len(line) and line[col].isnumeric()):
                num += line[col]
                col += 1
            if check_adj_symbols(symbol_locs, start_col, col - 1, row, max_row, max_col):
                part_num_sum += int(num)
            check_adj_gears(gear_locs, start_col, col - 1, row, max_row, max_col, int(num))
        col += 1
    row += 1
f.close()

print("The sum of part numbers is: " + str(part_num_sum))

# Now, calculate gears
gear_ratios = 0
for gear in gear_locs:
    adj_nums = gear_locs.get(gear)
    if (len(adj_nums) == 2):
        gear_ratios += (adj_nums[0]*adj_nums[1])

print("The sum of all gear ratios is: " + str(gear_ratios))