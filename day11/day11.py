# File for day 11 of AoC 2023
# Written by Joshua Yeaton on 12/11/2023

file_name = 'data.txt'
# file_name = 'data-test.txt'

f = open(file_name)

expanded_galaxy = []

# Find rows with no galaxies and coords of galaxies
row = 0
empty_rows = []
galaxies = []
for line in f:
    line = line.strip()
    found_gal = False
    expanded_galaxy.append(list(line))
    col = 0
    for c in line:
        if c == '#':
            found_gal = True
            galaxies.append((row,col))
        col += 1
    if not found_gal:
        empty_rows.append(row)
    row += 1
empty_rows.sort(reverse=True)

# Find columns with no galaxies
empty_cols = []
for i in range(len(line)):
    col = [row[i] for row in expanded_galaxy]
    found_gal = False
    for c in col:
        if c == '#':
            found_gal = True
    if not found_gal:
        empty_cols.append(i)
empty_cols.sort(reverse=True)

# Now, find the actual galaxy coordinates
# dist = 2
dist = 1000000
actual_gals = []
for g in galaxies:
    addl_rows = 0
    for r in empty_rows:
        if g[0] > r:
            addl_rows += 1
    addl_cols = 0
    for c in empty_cols:
        if g[1] > c:
            addl_cols += 1
    actual_rows = addl_rows * (dist - 1) + g[0]
    actual_cols = addl_cols * (dist - 1) + g[1]
    actual_gals.append((actual_rows, actual_cols))

# find our distances
total_dist = 0
total_gals = len(actual_gals)
for gal_1 in range(total_gals):
    for gal_2 in range(gal_1 + 1, total_gals):
        total_dist += (abs(actual_gals[gal_1][0] - actual_gals[gal_2][0]) + abs(actual_gals[gal_1][1] - actual_gals[gal_2][1]))

# solution
print(total_dist)

