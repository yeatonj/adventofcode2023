# File for day 17 of AoC 2023
# Written by Joshua Yeaton on 12/18/2023

import queue

# cur_loc = [path_length, task_number, (row, col), cur_dir, num_steps in dir]
def add_next_cells(cur_loc, path_queue, num_rows, num_cols, loss_map, cur_task_num):
    cur_path_len= cur_loc[0]
    cur_row = cur_loc[2][0]
    cur_col = cur_loc[2][1]
    cur_dir = cur_loc[3]
    cur_steps = cur_loc[4]
    # Get all possible cells we could travel to
    if cur_dir == '^':
        straight_loc = (cur_row - 1, cur_col)
        left_loc = (cur_row, cur_col - 1)
        right_loc = (cur_row, cur_col + 1)
        left_dir = '<'
        right_dir = '>'
    elif cur_dir == '>':
        straight_loc = (cur_row, cur_col + 1)
        left_loc = (cur_row - 1, cur_col)
        right_loc = (cur_row + 1, cur_col)
        left_dir = '^'
        right_dir = 'v'
    elif cur_dir == 'v':
        straight_loc = (cur_row + 1, cur_col)
        left_loc = (cur_row, cur_col + 1)
        right_loc = (cur_row, cur_col - 1)
        left_dir = '>'
        right_dir = '<'
    elif cur_dir == '<':
        straight_loc = (cur_row, cur_col - 1)
        left_loc = (cur_row + 1, cur_col)
        right_loc = (cur_row - 1, cur_col)
        left_dir = '^'
        right_dir = 'v'

    # Add left loc to queue (assuming it is on the grid)
    if (check_loc(left_loc, num_rows, num_cols)):
        new_path_len = cur_path_len + loss_map.get(left_loc)
        path_queue.put([new_path_len, cur_task_num + 1, left_loc, left_dir, 1])

    # Add right loc to queue
    if (check_loc(right_loc, num_rows, num_cols)):
        new_path_len = cur_path_len + loss_map.get(right_loc)
        path_queue.put([new_path_len, cur_task_num + 2, right_loc, right_dir, 1])

    # If we have < 3 steps in same direction, we can also go straight - add that to the queue
    if ((cur_steps < 3) and (check_loc(straight_loc, num_rows, num_cols))):
        new_path_len = cur_path_len + loss_map.get(straight_loc)
        path_queue.put([new_path_len, cur_task_num + 3, straight_loc, cur_dir, cur_path_len + 1])
    return

def check_loc(loc, num_rows, num_cols):
    row = loc[0]
    col = loc[1]
    if (row < 0 or
        row >= num_rows or
        col < 0 or col >= num_cols):
        return False
    return True

if __name__ == '__main__':
    file_name = 'data.txt'
    file_name = 'data-test.txt'

    f = open(file_name)

    loss_map = {}
    row = 0
    for line in f:
        line = line.strip()
        col= 0
        for c in line:
            loss_map.update({(row, col):int(c)})
            col += 1
        row += 1

    rows = row
    cols = col

    start = (0,0)
    goal = (rows -1, cols - 1)

    path_queue = queue.PriorityQueue()
    # To track state -> need current path length, (row, col), cur_dir, steps in dir
    # Add [path_length, task_number, (row, col), cur_dir, num_steps in dir]

    # Add the first two tasks manually
    start_1 = (1, 0)
    start_2 = (0, 1)
    path_queue.put([loss_map.get(start_1), 0, start_1, 'v', 1])
    path_queue.put([loss_map.get(start_2), 1, start_2, '>', 1])

    next_task_id = 2
    cur_loc = path_queue.get()
    while(cur_loc[2] != goal):
        add_next_cells(cur_loc, path_queue, rows, cols, loss_map, next_task_id)
        next_task_id += 3
        cur_loc = path_queue.get()
        print(cur_loc)
        

    

    f.close()