# File for day 12 of AoC 2023
# Written by Joshua Yeaton on 12/14/2023

# !!
def parse_line(line_in):
    split_line = line_in.split(' ')
    arrs = split_line[1].split(',')
    for i in range(len(arrs)):
        arrs[i] = int(arrs[i])
    return (split_line[0], tuple(arrs))

def calculate_arrangements(line, spring_count):
    found_dic = {}
    return recursive_calc_arr(line, spring_count, found_dic)

# found dic is a tuple of (line, spring_count)
def recursive_calc_arr(line_in, spring_count, found_dic):
    # remove leading and trailing .'s
    line = line_in.strip('.')
    # Check memoization dictionary
    if (line, spring_count) in found_dic:
        return found_dic.get((line,spring_count))
    # Base case 1, if we are looking for a single value, find matches
    if len(spring_count) == 1:
        res = count_matches(line, spring_count)
        # update the memoization dic
        found_dic.update({(line, spring_count):res})
        return res
    # Base case 2, if we are looking for multiple, string needs to be at least 3 chars long
    elif len(line) < 3:
        return 0
    # Otherwise, we need to split the string on all possible values starting from index [1] and ending at [-1]
    split_sum = 0
    tested_splits = []
    prods = []
    for split_ind in range(1, len(line) - 1):
        # print('split index is: ' + str(split_ind))
        split_prod = 0
        sub_prods = []
        if line[split_ind] != '#':
            # This is a valid index to split on
            left_str = line[0:split_ind]
            right_str = line[split_ind + 1:]
            left_str = left_str.strip('.')
            right_str = right_str.strip('.')
            if (left_str, right_str) not in tested_splits:
                tested_splits.append((left_str, right_str))
            else:
                continue
            # call recursive calc_arr on each split of the spring_count
            for i in range(1, len(spring_count)):
                left_springs = spring_count[0:i]
                right_springs = spring_count[i:]
                left_ans = recursive_calc_arr(left_str, left_springs, found_dic)
                right_ans = recursive_calc_arr(right_str, right_springs, found_dic)
                # Take the product to get the total number of valid combinations
                # print(left_str)
                # print(left_springs)
                # print(left_ans)
                # print(right_str)
                # print(right_springs) # error is in here with the longer arr, re
                # print(right_ans)
                # print()
                split_prod = left_ans * right_ans
                print('Product of split is: ' + str(split_prod))
                sub_prods.append(split_prod)
                print(sub_prods)
        prods.append(sum(sub_prods))
        print()
        print('Prods is: ')
        print(prods)
        # print(prods)
        split_sum += split_prod
    # Update memoization dictionary
    found_dic.update({(line, spring_count):split_sum})
    # And return
    return split_sum

# Note, this will always start with either ? or #
def count_matches(line, spring_count):
    num_spr = spring_count[0]
    # Split against .'s to get rid of them
    words = line.split('.')
    # Check how many have hashes
    has_hash = []
    for i in range(len(words)):
        if '#' in words[i]:
            has_hash.append(i)
    if len(has_hash) > 1:
        return 0
    if len(has_hash) == 1:
        # check just word with hash
        return check_word(words[has_hash[0]], num_spr)
    else:
        total = 0
        for w in words:
            total += check_word(w, num_spr)
        return total
    
# returns number of matches in a single word, consisting only of ? and #
def check_word(word, num_springs):
    # check to make sure it is even possible
    if num_springs > len(word):
        return 0
    # find first and last #, if they exist
    first_hash = -1
    last_hash = -1
    for i in range(len(word)):
        if word[i] == '#':
            if first_hash == -1:
                first_hash = i
                last_hash = i
            else:
                last_hash = i
    if first_hash == -1:
        # Case 1, all ?
        count = len(word) - num_springs + 1
        # print(word)
        # print('Number of springs is: ' + str(num_springs))
        # print('Count is: ' + str(count))
        # print()
    elif first_hash == last_hash:
        # Case 2, one hash
        top_range = first_hash + num_springs - 1
        bot_range = first_hash - num_springs + 1
        if top_range > len(word) - 1:
            top_range = len(word) - 1
        if bot_range < 0:
            bot_range = 0
        count = ((top_range + 1) - bot_range) - num_springs + 1
        # print(word)
        # print('Top range is: ' + str(top_range))
        # print('Bottom range is: ' + str(bot_range))
        # print('Number of springs is: ' + str(num_springs))
        # print('Count is: ' + str(count))
        # print()
    else:
        # Case 3, multiple hashes
        spacing = last_hash - first_hash
        if spacing > num_springs:
            return 0
        # we now know we need to include all of them, and it is possible
        top_range = first_hash + num_springs - 1
        bot_range = last_hash - num_springs + 1
        if top_range > len(word) - 1:
            top_range = len(word) - 1
        if bot_range < 0:
            bot_range = 0
        count = ((top_range + 1) - bot_range) - num_springs + 1
        # print(word)
        # print('Top range is: ' + str(top_range))
        # print('Bottom range is: ' + str(bot_range))
        # print('Spacing is: ' + str(spacing))
        # print('Number of springs is: ' + str(num_springs))
        # print('Count is: ' + str(count))
        # print()
    if count > 0:
        return count
    else:
        return 0 




if __name__ == '__main__':
    filename = 'data.txt'
    filename = 'data-test.txt'

    f = open(filename)

    lines = []
    springs = []

    total = 0

    for line in f:
        (line, spring) = parse_line(line.strip())
        lines.append(line)
        springs.append(spring)

        total += calculate_arrangements(line, spring)

    print('Solution is: ' + str(total))

    f.close()

# Answer of 6468 is too low