# File for day 12 of AoC 2023
# Written by Joshua Yeaton on 12/14/2023

# Redo. We write is_valid recursively - it looks for a match with hashes, then passes rest of word to next level. Returns 1 if OK, 0 if not.
# We then write the rec_calc_arr to take the first letter

def parse_line(line_in, copies):
    split_line = line_in.split(' ')
    arrs = split_line[1].split(',')
    for i in range(len(arrs)):
        arrs[i] = int(arrs[i])
    line_out = ''
    for i in range(copies):
        line_out += split_line[0] + '?'
    line_out = line_out[:-1]
    return (line_out, tuple(arrs) * copies)

def calculate_arrangements(line, spring_count, found_dic):
    line_in = line[0]
    cur_char = line[0]
    for i in range(1,len(line)):
        if cur_char == '.' and line[i] == '.':
            continue
        else:
            cur_char = line[i]
            line_in += cur_char
    # print(line_in)
    return recursive_calc_arr(line_in, spring_count, found_dic)

# found dic is a tuple of (line, spring_count)
def recursive_calc_arr(line_in, spring_count, found_dic):
    # remove leading and trailing .'s
    line = line_in.strip('.')
    
    # Check memoization dictionary
    if (line, spring_count) in found_dic:
        return found_dic.get((line,spring_count))
    ## Base cases
    # Base case 1:
    if len(spring_count) == 0:
        if check_no_rem_hashes(line):
            found_dic.update({(line,spring_count):1})
            return 1
        else:
            found_dic.update({(line,spring_count):0})
            return 0
    
    cur_springs = spring_count[0]
    
    # Base case 2: length of line is less than number of springs left
    if len(line) < cur_springs:
        found_dic.update({(line,spring_count):0})
        return 0

    # !! Regular cases
    cur_ind = 0
    # Reg case 1: we start w/ hash - this means we have to match with the next word
    if line[cur_ind] == '#':
        # look for first non-hash value
        while cur_ind < len(line) and line[cur_ind] == '#' and cur_ind < cur_springs:
            cur_ind += 1
        # At this point, we either are at correct word length for current spring, we have a non-hash next char, or we are out of space
        if cur_ind == cur_springs:
            # we have a match! call the function again, reducing the size of the word
            if cur_ind == len(line):
                if len(spring_count) == 1:
                    # !! update memoization dictionary
                    found_dic.update({(line,spring_count):1})
                    return 1
                else:
                    # !! update memoization dictionary
                    found_dic.update({(line,spring_count):0})
                    return 0
            else:
                if line[cur_ind] == '#': # word too large!
                    # update memoization dictionary
                    found_dic.update({(line,spring_count):0})
                    return 0
                # else, ? or ., we treat both as . !! check this logic!
                # !! update memoization dictionary
                ans = recursive_calc_arr(line[cur_ind + 1:], spring_count[1:], found_dic)
                found_dic.update({(line,spring_count):ans})
                return ans
        elif cur_ind == len(line):
            # we ran out of space, return 0
            # !! update memoization dictionary
            found_dic.update({(line,spring_count):0})
            return 0
        elif line[cur_ind] == '.':
            # not possible to make this word, return 0
            # !! update memoization dictionary
            found_dic.update({(line,spring_count):0})
            return 0
        # else, we have cur_ind pointing to a ?, which must be a # in order to match
        elif line[cur_ind] == '?':
            # repl
            new_line = line[0:cur_ind] + '#' + line[cur_ind + 1:]
            # !! update memoization dictionary
            ans = recursive_calc_arr(new_line, spring_count, found_dic)
            found_dic.update({(line,spring_count):ans})
            return ans
        else:
            print('Unexpected character in line...')
            exit()
    # Else, we are starting the line with a ?. Try both possibilities
    dot_line = '.' + line[1:]
    hash_line = '#' + line[1:]
    dot_combos = recursive_calc_arr(dot_line, spring_count, found_dic)
    hash_combos = recursive_calc_arr(hash_line, spring_count, found_dic)
    # update memoization dictionary
    ans = (dot_combos + hash_combos)
    found_dic.update({(line,spring_count):ans})
    return ans




# Function to make sure there are no hashes left in a line. Returns True if there are only . and ?
def check_no_rem_hashes(line):
    for c in line:
        if c == '#':
            return False
    return True




if __name__ == '__main__':
    filename = 'data.txt'
    # filename = 'data-test.txt'

    f = open(filename)

    lines = []
    springs = []

    total = 0

    i = 0
    found_dic = {}
    for line in f:
        # copies = 1 # Part 1
        copies = 5 # Part 2
        (line, spring) = parse_line(line.strip(), copies)
        lines.append(line)
        springs.append(spring)

        total += calculate_arrangements(line, spring, found_dic)
        i += 1
        print(i)

    print('Solution is: ' + str(total))
    # Part 1 solution is 7705
    # Part 2 solution is 50338344809230

    f.close()