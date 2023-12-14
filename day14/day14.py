# File for day 14 of AoC 2023
# Written by Joshua Yeaton on 12/14/2023

# function used to roll rocks in an array
def roll_rocks(pos_arr, dir):
    if dir == 'n':
        # Get each column
        for col_num in range(len(pos_arr[0])):
            cur_col = [row[col_num] for row in pos_arr]
            new_col = roll_array(cur_col)
            for r in range(len(new_col)):
                pos_arr[r][col_num] = new_col[r]
    elif dir == 's':
        # Get each column
        for col_num in range(len(pos_arr[0])):
            cur_col = [row[col_num] for row in pos_arr]
            cur_col.reverse()
            new_col = roll_array(cur_col)
            new_col.reverse()
            for r in range(len(new_col)):
                pos_arr[r][col_num] = new_col[r]
    elif dir == 'w':
        for i in range(len(pos_arr)):
            new_row = roll_array(pos_arr[i])
            pos_arr[i] = new_row
    else: # e
        for i in range(len(pos_arr)):
            temp_row = pos_arr[i]
            temp_row.reverse()
            new_row = roll_array(temp_row)
            new_row.reverse()
            pos_arr[i] = new_row
    return pos_arr

# Always rolls towards index 0
def roll_array(arr_in):
    # Move the top to the first blank index
    cur_top = 0
    search_ind = 0
    arr_len = len(arr_in)
    while (search_ind < arr_len):
        while(cur_top < arr_len and arr_in[cur_top] != '.'):
            cur_top += 1
        if (search_ind < cur_top + 1):
            search_ind = cur_top + 1
        # at this point, we know current top is one below search index
        while (search_ind < arr_len):
            if (arr_in[search_ind] == '.'):
                search_ind += 1
            elif (arr_in[search_ind] == 'O'):
                arr_in[cur_top] = 'O'
                arr_in[search_ind] = '.'
                cur_top += 1
                search_ind += 1
            elif (arr_in[search_ind] == '#'):
                # reset cur_top
                cur_top = search_ind + 1
                search_ind = search_ind + 1
                break # to make sure we fully reset
    return arr_in

def calc_load(dish_status):
    total_load = 0
    row_weight = len(dish_status)
    for row in dish_status:
        for c in row:
            if c == 'O':
                total_load += row_weight
        row_weight -= 1
    return total_load


if __name__ == "__main__":
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    f = open(file_name)

    cur_dish_stat = []
    for line in f:
        cur_dish_stat.append(list(line.strip()))

    # # Part 1
    # new_dish_stat = roll_rocks(cur_dish_stat,'n')

    # Part 2
    cur_vals = []
    ref_vals = []
    vals_to_track = 100
    ref_start = 5000
    new_dish_stat = cur_dish_stat   
    target_iters = 1000000000
    interval = -1
    for i in range(1, target_iters):
        new_dish_stat = roll_rocks(new_dish_stat,'n')
        new_dish_stat = roll_rocks(new_dish_stat,'w')
        new_dish_stat = roll_rocks(new_dish_stat,'s')
        new_dish_stat = roll_rocks(new_dish_stat,'e')

        if i % 1000 == 0:
            print(i)

        # Check for periodicity
        if (i > ref_start - vals_to_track):
            load = calc_load(new_dish_stat)
            if len(cur_vals) == vals_to_track:
                cur_vals.pop(0)
            cur_vals.append(load)
        # Copy at value
        if i == ref_start:
            for val in cur_vals:
                ref_vals.append(val)
        if i > ref_start:
            if cur_vals == ref_vals:
                interval = i - ref_start
                offset_from_zero = target_iters % interval
        if ((interval > 0) and ((i - offset_from_zero) % interval == 0)):
            break
    
    # # For printing
    # for row in range(len(new_dish_stat)):
    #     for col in range(len(new_dish_stat[0])):
    #         print(new_dish_stat[row][col], end='')
    #     print()

    load = calc_load(new_dish_stat)

    print('Solution: ' + str(load))
    

    f.close()
