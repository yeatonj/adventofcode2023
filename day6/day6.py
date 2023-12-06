# File for day 6 of AoC 2023
# Written by Joshua Yeaton on 12/6/2023

f_name = 'data.txt'
# f_name = 'data-test.txt'

f = open(f_name)

times = []
distances= []
all_trial_wins = []

# Extract the data - first the times
line = f.readline()
line = line.strip()
line_split = line.split(' ')
for entry in line_split:
    if entry.isnumeric():
        times.append(int(entry))
# And now the distances
line = f.readline()
line = line.strip()
line_split = line.split(' ')
for entry in line_split:
    if entry.isnumeric():
        distances.append(int(entry))

# Now check the possible races
for i in range(len(times)):
    trial_wins = 0
    for j in range(1, times[i]):
        speed = j
        time_rem = times[i] - j
        if (time_rem * speed > distances[i]):
            trial_wins += 1
    all_trial_wins.append(trial_wins)

# Find the products
prod = 1
for win_count in all_trial_wins:
    prod *= win_count

print("Solution to part 1: " + str(prod))

f.close()

# Begin part 2
f = open(f_name)

time = ''
distance = ''

# Extract the data - first the times
line = f.readline()
line = line.strip()
line_split = line.split(' ')
for entry in line_split:
    if entry.isnumeric():
        time += entry
# And now the distances
line = f.readline()
line = line.strip()
line_split = line.split(' ')
for entry in line_split:
    if entry.isnumeric():
        distance += entry

time = int(time)
distance = int(distance)

wins = 0
for j in range(1, time):
    speed = j
    time_rem = time - j
    if (time_rem * speed > distance):
        wins += 1

print('Solution to part 2: ' + str(wins))


f.close()