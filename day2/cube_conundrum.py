# File for day 2 of AoC 2023
# Written by Joshua Yeaton on 12/2/2023

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

MAX_TOTAL_CUBES = MAX_BLUE + MAX_GREEN + MAX_RED


def check_game(game_row_split):
    min_red = 0
    min_blue = 0
    min_green = 0
    possible = True
    subgames = game_row_split.split(';')

    for subgame in subgames:
        if subgame[0] == ' ':
            subgame = subgame[1:]

        split_subgame = subgame.split()

        red_cubes = 0
        green_cubes = 0
        blue_cubes = 0
        for i in range(0,len(split_subgame),2):
            if (split_subgame[i+1] == 'green' or split_subgame[i+1] == 'green,'):
                green_cubes += int(split_subgame[i])
            elif (split_subgame[i+1] == 'red' or split_subgame[i+1] == 'red,'):
                red_cubes += int(split_subgame[i])
            else:
                blue_cubes += int(split_subgame[i])

            cube_sum = green_cubes + red_cubes + blue_cubes

            if (red_cubes > MAX_RED or green_cubes > MAX_GREEN or blue_cubes > MAX_BLUE or cube_sum > MAX_TOTAL_CUBES):
                possible = False
            
            if red_cubes > min_red:
                min_red = red_cubes
            if green_cubes > min_green:
                min_green = green_cubes
            if blue_cubes > min_blue:
                min_blue = blue_cubes
    return (possible, min_red, min_blue, min_green)


# f = open('data-test.txt')
f = open('data.txt')

id_sum = 0
power_sum = 0

for line in f:
    line_split = line.split()
    game_num = int(line_split[1][:-1])

    game_details = ' '.join(line_split[2:])

    (poss, red, green, blue) = check_game(game_details)

    if poss:
        id_sum += game_num
    power_sum += (red*green*blue)

print("The sum of the game id's of all possible games is: " + str(id_sum))
print("The sum of all possible powers is: " + str(power_sum))