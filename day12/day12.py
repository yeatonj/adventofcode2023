# File for day 12 of AoC 2023
# Written by Joshua Yeaton on 12/14/2023

# !!
def parse_line(line_in):
    split_line = line_in.split(' ')
    arrs = split_line[1].split(',')
    for i in range(len(arrs)):
        arrs[i] = int(arrs[i])
    return (split_line[0], arrs)

def calculate_arrangements(line, spring_count):
    found_dic = {}
    return recursive_calc_arr(line, spring_count, found_dic)


def recursive_calc_arr(line, spring_count, found_dic):
    print(line)
    print(is_valid(line, spring_count))
    # Check the memoization dict
    if line in found_dic:
        return found_dic.get(line)
    # Check if line is valid
    if not is_valid(line, spring_count):
        return 0
    # Find the first '?'
    found_quest = False
    for i in range(len(line)):
        if line[i] == '?':
            found_quest = True
            break
    # If this is complete line, return this value
    if not found_quest:
        found_dic.update({line:1})
        return 1
    # At this point, we need to check the two options
    temp_sum = 0
    temp_line = list(line)
    temp_line[i] = '.'
    per_line = ''.join(temp_line)
    temp_line[i] = '#'
    hash_line = ''.join(temp_line)
    # Now, we can test our two lines
    temp_sum += recursive_calc_arr(per_line, spring_count, found_dic)
    temp_sum += recursive_calc_arr(hash_line, spring_count, found_dic)
    found_dic.update({line:temp_sum})
    return temp_sum

    

def is_valid(line, spring_count):
    cur_ind = 0
    str_len = len(line)
    for val in spring_count:
        found = False
        while (not found):
            if (cur_ind > 0):
                if (cur_ind < str_len and line[cur_ind - 1] == '#'):
                    return False
            if ((cur_ind + val) > str_len):
                return False
            elif (line[cur_ind] == '?'):
                found = True
                for offset in range(0, val):
                    if (line[cur_ind + offset] == '.'):
                        cur_ind += 1
                        found = False
                        break
                # Check to make sure that the next index isn't #
                if ((cur_ind + offset + 1 < str_len) and (line[cur_ind + offset + 1] == '#')):
                    cur_ind += 1
                    found = False
                if found:
                    # !! find the next possible start point
                    cur_ind += offset + 2
                    if (cur_ind - 1 < str_len and line[cur_ind - 1] == '#'):
                        return False
            elif (line[cur_ind] == '#'):
                found = True
                for offset in range(0, val):
                    if (line[cur_ind + offset] == '.'):
                        cur_ind += 1
                        found = False
                        break
                # Check to make sure that the next index isn't #
                if ((cur_ind + offset + 1 < str_len) and (line[cur_ind + offset + 1] == '#')):
                    cur_ind += 1
                    found = False
                if found:
                    # !! find the next possible start point
                    cur_ind += offset + 2
                    if (cur_ind - 1 < str_len and line[cur_ind - 1] == '#'):
                        return False
            else: 
                cur_ind += 1
    return True




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