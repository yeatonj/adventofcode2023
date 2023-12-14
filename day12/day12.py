# File for day 12 of AoC 2023
# Written by Joshua Yeaton on 12/14/2023

# !!
def parse_line(line_in):
    split_line = line_in.split(' ')
    arrs = split_line[1].split(',')
    for i in range(len(arrs)):
        arrs[i] = int(arrs[i])
    return (split_line[0], arrs)

# !!
def calculate_arrangements(line, spring_count):
    return 1

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