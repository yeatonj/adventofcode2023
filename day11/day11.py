# File for day 11 of AoC 2023
# Written by Joshua Yeaton on 12/11/2023

file_name = 'data.txt'
file_name = 'data-test.txt'

f = open(file_name)

expanded_galaxy = []

# Find rows with no galaxies
for line in f:
    line = line.strip()
    found_gal = False
    expanded_galaxy.append(list(line))
    for c in line:
        if c == '#':
            found_gal = True
            break
#     if not found_gal:
#         # Insert the galaxy
#         expanded_galaxy.append(list(line))
    
# # Find columns with no galaxies
# insert_cols = []
# for i in range(len(line)):
#     col = [row[i] for row in expanded_galaxy]
#     found_gal = False
#     for c in col:
#         if c == '#':
#             found_gal = True
#     if not found_gal:
#         insert_cols.append(i)

# # Now, add those columns
# insert_cols.sort(reverse=True)
# for line in expanded_galaxy:
#     for col in insert_cols:
#         line.insert(col, '.')

# Now, save the coordinates of each galaxy into a list
rows = len(expanded_galaxy)
cols = len(expanded_galaxy[0])
galaxies = []
for r in range(rows):
    for c in range(cols):
        if expanded_galaxy[r][c] == '#':
            galaxies.append((r,c))

total_dist = 0
total_gals = len(galaxies)
for gal_1 in range(total_gals):
    for gal_2 in range(gal_1 + 1, total_gals):
        total_dist += (abs(galaxies[gal_1][0] - galaxies[gal_2][0]) + abs(galaxies[gal_1][1] - galaxies[gal_2][1]))

# Part 1 solution
print(total_dist)

