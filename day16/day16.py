# File for day 16 of AoC 2023
# Written by Joshua Yeaton on 12/18/2023

import queue

def add_next_locs(cur_loc, num_rows, num_cols, to_visit, visited, t_contents):
    # make sure we haven't been to this exact location
    if cur_loc in visited:
        return
    visited.update({cur_loc:1})
    cur_row = cur_loc[0]
    cur_col = cur_loc[1]
    cur_dir = cur_loc[2]
    # First, check to make sure we're not headed off the grid, if so, simply return
    if ((cur_dir == '<' and cur_col == 0) or 
        (cur_dir == '^' and cur_row == 0) or
        (cur_dir == 'v' and cur_row == num_rows - 1) or
        (cur_dir == '>' and cur_col == num_cols - 1)):
        return
    # otherwise, we know we are doing something
    if cur_dir == '<':
        next_cell = (cur_row, cur_col - 1)
    elif cur_dir == '^':
        next_cell = (cur_row - 1, cur_col)
    elif cur_dir == 'v':
        next_cell = (cur_row + 1, cur_col)
    else:
        next_cell = (cur_row, cur_col + 1)
    next_contents = t_contents.get(next_cell)
    if (next_contents == '.'):
        # keep on going!
        to_visit.put((next_cell[0], next_cell[1], cur_dir))
    elif (next_contents == '/'):
        if cur_dir == '<':
            to_visit.put((next_cell[0], next_cell[1], 'v'))
        elif cur_dir == '^':
            to_visit.put((next_cell[0], next_cell[1], '>'))
        elif cur_dir == 'v':
            to_visit.put((next_cell[0], next_cell[1], '<'))
        else:
            to_visit.put((next_cell[0], next_cell[1], '^'))
    elif (next_contents == '\\'):
        if cur_dir == '<':
            to_visit.put((next_cell[0], next_cell[1], '^'))
        elif cur_dir == '^':
            to_visit.put((next_cell[0], next_cell[1], '<'))
        elif cur_dir == 'v':
            to_visit.put((next_cell[0], next_cell[1], '>'))
        else:
            to_visit.put((next_cell[0], next_cell[1], 'v'))
    elif (next_contents == '|'):
        if cur_dir == '<' or cur_dir == '>':
            to_visit.put((next_cell[0], next_cell[1], '^'))
            to_visit.put((next_cell[0], next_cell[1], 'v'))
        else:
            to_visit.put((next_cell[0], next_cell[1], cur_dir))
    elif (next_contents == '-'):
        if cur_dir == '^' or cur_dir == 'v':
            to_visit.put((next_cell[0], next_cell[1], '<'))
            to_visit.put((next_cell[0], next_cell[1], '>'))
        else:
            to_visit.put((next_cell[0], next_cell[1], cur_dir))
    return

          


if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    f = open(file_name)

    t_contents = {}

    row = 0
    for line in f:
        line = line.strip()
        col = 0
        for c in line:
            t_contents.update({(row, col):c})
            col +=1
        row += 1

    num_rows = row
    num_cols = col

    # print(t_contents)

    # use a queue to enqueue which to visit, with (row, col, dir) holding the dirs
    # store in a dic, if already present in dic, we don't enqueue the next place to visit

    to_visit = queue.Queue()
    # note, we start off map. Should really remove this, but it makes the implementation correct if we subtract 1
    to_visit.put((0,-1,'>'))

    visited = {}

    while (not to_visit.empty()):
        # Get our current location and direction
        cur_loc = to_visit.get()

        # Find and add the next locations to the queue
        add_next_locs(cur_loc, num_rows, num_cols, to_visit, visited, t_contents)

    # At this point, visited contains all cells and directions, but we need to do only unique visits
    unique_visits = {}
    for visited_cell in visited:
        if ((visited_cell[0], visited_cell[1]) not in unique_visits):
            unique_visits.update({(visited_cell[0], visited_cell[1]):1})
    print('Part 1 solution is: ' + str(len(unique_visits) - 1))

    # Start of part 2---------------------------------------------------
    # now calculate the max number of energized cells
    max_energized = 0
    # Top row
    for i in range(num_cols):
        visited = {}
        to_visit = queue.Queue()
        to_visit.put((-1,i,'v'))
        while (not to_visit.empty()):
            cur_loc = to_visit.get()
            # Find and add the next locations to the queue
            add_next_locs(cur_loc, num_rows, num_cols, to_visit, visited, t_contents)
        unique_visits = {}
        for visited_cell in visited:
            if ((visited_cell[0], visited_cell[1]) not in unique_visits):
                unique_visits.update({(visited_cell[0], visited_cell[1]):1})
        num_energized = len(unique_visits) - 1
        if num_energized > max_energized:
            max_energized = num_energized
    # Bottom row
    for i in range(num_cols):
        visited = {}
        to_visit = queue.Queue()
        to_visit.put((num_rows,i,'^'))
        while (not to_visit.empty()):
            cur_loc = to_visit.get()
            # Find and add the next locations to the queue
            add_next_locs(cur_loc, num_rows, num_cols, to_visit, visited, t_contents)
        unique_visits = {}
        for visited_cell in visited:
            if ((visited_cell[0], visited_cell[1]) not in unique_visits):
                unique_visits.update({(visited_cell[0], visited_cell[1]):1})
        num_energized = len(unique_visits) - 1
        if num_energized > max_energized:
            max_energized = num_energized
    # Left column
    for i in range(num_rows):
        visited = {}
        to_visit = queue.Queue()
        to_visit.put((i,-1,'>'))
        while (not to_visit.empty()):
            cur_loc = to_visit.get()
            # Find and add the next locations to the queue
            add_next_locs(cur_loc, num_rows, num_cols, to_visit, visited, t_contents)
        unique_visits = {}
        for visited_cell in visited:
            if ((visited_cell[0], visited_cell[1]) not in unique_visits):
                unique_visits.update({(visited_cell[0], visited_cell[1]):1})
        num_energized = len(unique_visits) - 1
        if num_energized > max_energized:
            max_energized = num_energized
    # Right column
    for i in range(num_rows):
        visited = {}
        to_visit = queue.Queue()
        to_visit.put((i,num_cols,'<'))
        while (not to_visit.empty()):
            cur_loc = to_visit.get()
            # Find and add the next locations to the queue
            add_next_locs(cur_loc, num_rows, num_cols, to_visit, visited, t_contents)
        unique_visits = {}
        for visited_cell in visited:
            if ((visited_cell[0], visited_cell[1]) not in unique_visits):
                unique_visits.update({(visited_cell[0], visited_cell[1]):1})
        num_energized = len(unique_visits) - 1
        if num_energized > max_energized:
            max_energized = num_energized
            

    print('Part 2 Solution: ' + str(max_energized))
            

    f.close()