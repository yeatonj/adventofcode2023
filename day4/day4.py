# File for day 4 of AoC 2023
# Written by Joshua Yeaton on 12/4/2023

fname = 'data.txt'
# fname = 'data-test.txt'
f = open(fname)

# create array for the number of cards
card_count = []
for line in f:
    card_count.append(1)

f.close()

# Reopen the file and calculate total points
f = open(fname)
total_points = 0
cur_card = 0
for line in f:
    line_points = 0
    line_win_count = 0
    entries = line.split('|')
    # First, extract the winning numbers
    winning_nums = ''.join(entries[0])
    winning_nums = winning_nums.split(':')
    winning_nums = ''.join(winning_nums[1])
    winning_nums = winning_nums.strip()
    winning_nums = winning_nums.split(' ')

    # Then, extract the selected numbers
    selected_nums = entries[1].strip()
    selected_nums = selected_nums.split(' ')
    while ('' in selected_nums):
        selected_nums.remove('')
    
    # now calculate the points
    for guess in selected_nums:
        if ((guess in winning_nums) and (line_points == 0)):
            line_win_count += 1
            line_points = 1
        elif (guess in winning_nums):
            line_win_count += 1
            line_points *= 2
    # now, add the copies of cards we've won to the total number of cards we have
    i = cur_card + 1
    while ((i < len(card_count)) and (line_win_count > 0)):
        card_count[i] += card_count[cur_card]
        line_win_count -= 1
        i += 1
    total_points += line_points
    cur_card += 1

print('Total points: ' + str(total_points))
print('Total cards: ' + str(sum(card_count)))

f.close()