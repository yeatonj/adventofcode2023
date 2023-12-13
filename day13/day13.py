# File for day 13 of AoC 2023
# Written by Joshua Yeaton on 12/13/2023

# returns a tuple with the row and column of the reflection
def find_reflections(pattern, rows, cols, part_2):
    # Search through rows. If we find a pair, check successive outer pairs
    for i in range(1,rows):
        if check_paired_row(pattern, i - 1, i, rows, part_2):
            return (i, 0)
    # Search through cols. If we find a pair, check successive outer pairs
    for i in range(1,cols):
        if check_paired_col(pattern, i - 1, i, cols, part_2):
            return (0, i)
    return -1

    

# Checks a paired row, called recursively
def check_paired_row(pattern, cur_up_row, cur_down_row, max_row, part_2):
    if part_2:
        return check_paired_row_2(pattern, cur_up_row, cur_down_row, max_row, False)
    # Base case 1: outside max rows - success
    if ((cur_up_row < 0) or (cur_down_row >= max_row)):
        return True
    # recursive case 1 - match
    if (pattern[cur_up_row] == pattern[cur_down_row]):
        return check_paired_row(pattern, cur_up_row - 1, cur_down_row + 1, max_row, part_2)
    else:
        return False
    
def check_paired_row_2(pattern, cur_up_row, cur_down_row, max_row, found_smear):
    # Base case 1: outside max rows with smear - success
    if (((cur_up_row < 0) or (cur_down_row >= max_row)) and found_smear):
        return True
    # Base case 2: outside max rows without smear - fail
    if (((cur_up_row < 0) or (cur_down_row >= max_row)) and not found_smear):
        return False
    # recursive case 1 - match without smear
    if (pattern[cur_up_row] == pattern[cur_down_row]):
        return check_paired_row_2(pattern, cur_up_row - 1, cur_down_row + 1, max_row, found_smear)
    # recursive case 2 - no match, already found smear
    if found_smear:
        return False
    # recursive case 3 - no match, haven't already found smear
    no_match = 0
    cur_col = 0
    while (no_match <= 1 and cur_col < len(pattern[0])):
        if pattern[cur_up_row][cur_col] != pattern[cur_down_row][cur_col]:
            no_match += 1
        cur_col += 1
    if no_match == 1: # found a single smear
        return check_paired_row_2(pattern, cur_up_row - 1, cur_down_row + 1, max_row, True)
    return False
    
# Checks a paired col, called recursively
def check_paired_col(pattern, cur_left_col, cur_right_col, max_col, part_2):
    if part_2:
        return check_paired_col_2(pattern, cur_left_col, cur_right_col, max_col, False)
    # Base case 1: outside max rows - success
    if ((cur_left_col < 0) or (cur_right_col >= max_col)):
        return True
    # get columns
    left_col = [row[cur_left_col] for row in pattern]
    right_col = [row[cur_right_col] for row in pattern]
    # recursive case 1 - match
    if (left_col == right_col):
        return check_paired_col(pattern, cur_left_col - 1, cur_right_col + 1, max_col, part_2)
    else:
        return False
    
def check_paired_col_2(pattern, cur_left_col, cur_right_col, max_col, found_smear):
    # Base case 1: outside max rows with smear - success
    if (((cur_left_col < 0) or (cur_right_col >= max_col)) and found_smear):
        return True
    # Base case 2: outside max rows without smear - fail
    if (((cur_left_col < 0) or (cur_right_col >= max_col)) and not found_smear):
        return False
    # get columns
    left_col = [row[cur_left_col] for row in pattern]
    right_col = [row[cur_right_col] for row in pattern]
    # recursive case 1 - match without smear
    if (left_col == right_col):
        return check_paired_col_2(pattern, cur_left_col - 1, cur_right_col + 1, max_col, found_smear)
    # recursive case 2 - no match, already found smear
    if found_smear:
        return False
    # recursive case 3 - no match, haven't already found smear
    no_match = 0
    cur_row = 0
    while (no_match <= 1 and cur_row < len(left_col)):
        if left_col[cur_row] != right_col[cur_row]:
            no_match += 1
        cur_row += 1
    if no_match == 1: # found a single smear
        return check_paired_col_2(pattern, cur_left_col - 1, cur_right_col + 1, max_col, True)
    return False



if __name__ == "__main__":
    file_name = 'data.txt'
    # file_name = 'data-test.txt'
    # file_name = 'data-test-2.txt'
    part_2 = True

    f = open(file_name)

    cur_line = f.readline().strip()

    summary_val = 0

    while(cur_line):
        cur_pattern = [cur_line]
        cols = len(cur_line)
        cur_line = f.readline().strip()
        rows = 1
        while(cur_line):
            cur_pattern.append(cur_line)
            cur_line = f.readline().strip()
            rows += 1
        # Skip blank lines
        cur_line = f.readline().strip()
        # find reflections
        ref_val = find_reflections(cur_pattern, rows, cols, part_2)

        summary_val += ((ref_val[0] * 100) + ref_val[1])

    print('Answer: ' + str(summary_val))

    f.close()