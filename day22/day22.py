# File for day 22 of AoC 2023
# Written by Joshua Yeaton on 1/4/2024

def parse_input(file_name):
    f = open(file_name)

    block_dic = {}
    occupied = {}
    block_num = 0

    for line in f:
        block_num += 1
        line = line.strip()
        blocks = line.split('~')
        block0 = blocks[0].split(',')
        block1 = blocks[1].split(',')
        add_block(block0, block1, block_dic, block_num, occupied)
        
    f.close()
    return (block_dic, occupied)

def add_block(start, end, block_dic, block_num, occupied):
    start_int = tuple([int(num) for num in start])
    end_int = tuple([int(num) for num in end])
    # sort them to have end be greater
    if start_int > end_int:
        (start_int, end_int) = (end_int, start_int)
    if ((start_int[0] == end_int[0]) and (start_int[1] == end_int[1])):
        if (start_int[2] == end_int[2]):
            # all are the same, single block!
            block_dic.update({block_num:[start_int]})
            occupied.update({start_int:1})
            # !! add to occupied!
        else:
            # z axis is different, vertical block
            sub_blocks = []
            for i in range(start_int[2], end_int[2] + 1):
                new_block = (start_int[0], start_int[1], i)
                sub_blocks.append(new_block)
                occupied.update({new_block:1})
            block_dic.update({block_num:sub_blocks})
    elif ((start_int[0] == end_int[0]) and (start_int[2] == end_int[2])):
        # different on y-axis
        sub_blocks = []
        for i in range(start_int[1], end_int[1] + 1):
            new_block = (start_int[0], i, start_int[2])
            sub_blocks.append(new_block)
            occupied.update({new_block:1})
        block_dic.update({block_num:sub_blocks})
    else:
        # different on x-axis
        sub_blocks = []
        for i in range(start_int[0], end_int[0] + 1):
            new_block = (i, start_int[1], start_int[2])
            sub_blocks.append(new_block)
            occupied.update({new_block:1})
        block_dic.update({block_num:sub_blocks})
    return

def drop_brick(block_dic, brick_num, old_occupied, new_occupied):
    # remove the brick's coords from the old occupied
    curr_coords = block_dic.get(brick_num)
    for coord in curr_coords:
        old_occupied.pop(coord)
    # move down until we collide with a brick in new occupied or old occupied
    collision = False
    moved = 0
    while (not collision):
        new_coord = [(x, y, z - 1) for (x, y, z) in curr_coords]
        for coord in new_coord:
            if ((coord[2] == 0) or (coord in old_occupied) or (coord in new_occupied)):
                collision = True
                break
        if not collision:
            moved += 1
            curr_coords = new_coord

    # update the block dictionary and occupied
    block_dic.update({brick_num:curr_coords})
    for coord in curr_coords:
        new_occupied.update({coord:1})
    # if we moved the brick, return True, else return false
    if moved > 0:
        return True
    else:
        return False

def drop_all_bricks(block_dic, occupied):
    # deep copy the block dictionary to avoid mutating it
    block_dic_new = {}
    for block in block_dic:
        initial_blocks = block_dic.get(block)
        temp = [b for b in initial_blocks]
        block_dic_new.update({block:temp})
    any_movement = 0
    brick_moved = True
    while (brick_moved):
        brick_moved = False
        new_occupied = {}
        for brick_num in block_dic_new:
            if (drop_brick(block_dic_new, brick_num, occupied, new_occupied)):
                brick_moved = True
                any_movement += 1
        occupied = new_occupied
    return (any_movement, occupied, block_dic_new)



if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    (block_dic, occupied) = parse_input(file_name)

    # general thought process: hold all block positions in a dictionary
    # for each block, add current positions to an 'occupied' dictionary
    # Then, loop through every block, trying to move it down until it collides with something
    # add it to a 'new' dictionary, and check against both the new and old (remove from old at same time)
    
    # drop all bricks
    (moved, occupied, new_block_dic) = drop_all_bricks(block_dic, occupied)


    # Now, determine which are safe to remove. Remove each brick in turn
    ok_to_dis = 0
    num_moved = 0
    alt_moved = 0
    num_keys = len(new_block_dic)
    for i in range(1, num_keys + 1):
        # copy occupied
        temp_occupied = {}
        for e in occupied:
            temp_occupied.update({e:1})
        # save and pop the block
        coords = new_block_dic.get(i)
        new_block_dic.pop(i)
        # remove all from temp occupied
        for c in coords:
            temp_occupied.pop(c)

        # query the drop function
        (moved, temp_occ, temp_dic) = drop_all_bricks(new_block_dic, temp_occupied)
        
        # re add the block
        new_block_dic.update({i:coords})

        if not moved:
            ok_to_dis += 1
        else:
            # check to see how many moved
            num_moved += moved
            for i in range(1, num_keys + 1):
                old_brick = new_block_dic.get(i)
                new_brick = temp_dic.get(i)
                if new_brick == None:
                    continue
                for coord in old_brick:
                    if coord not in new_brick:
                        alt_moved += 1
                        break

    print(ok_to_dis)
    # print(num_moved)
    print(alt_moved) # this is the correct answer, not sure why.
    # Answer of 916 is too high
    # Answer of 465 is correct

    # Part 2:
    # Answer of 90992 is too high

        
    

    