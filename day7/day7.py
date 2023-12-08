# File for day 7 of AoC 2023
# Written by Joshua Yeaton on 12/8/2023

# General thought process - create a tuple for each hand.
# Go thru the entries in the hand and stick into temp dict - count dict
# entries to segment into the appropriate hand.
# Add to a list for each hand type, then sort and assign scores based on that

# Part 1 ---------------------------------------------------

file_name = 'data.txt'
# file_name = 'data-test.txt'

f = open(file_name)

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high = []

total_hands = 0

for line in f:
    total_hands += 1
    line = line.strip()
    split_l = line.split()
    card_dict = {}
    hand = split_l[0]
    score = int(split_l[1])
    hand_l = []
    for card in hand:
        # Add the card to the hand list
        if card.isnumeric():
            hand_l.append(int(card))
        elif card == 'T':
            hand_l.append(10)
        elif card == 'J':
            hand_l.append(11)
        elif card == 'Q':
            hand_l.append(12)
        elif card == 'K':
            hand_l.append(13)
        else:
            hand_l.append(14)
        if card not in card_dict:
            card_dict.update({card:1})
        else:
            card_dict.update({card:(card_dict.get(card) + 1)})
    hand_tup = (hand_l, score)
    # Add to the appropriate list
    # 5 of a kind
    if len(card_dict) == 1:
        five_kind.append(hand_tup)
    # four of a kind or full house
    elif len(card_dict) == 2:
        if 4 in card_dict.values():
            four_kind.append(hand_tup)
        else:
            full_house.append(hand_tup)
    #three of a kind or two pair
    elif len(card_dict) == 3:
        if 3 in card_dict.values():
            three_kind.append(hand_tup)
        else:
            two_pair.append(hand_tup)
    # one pair
    elif len(card_dict) == 4:
        one_pair.append(hand_tup)
    # high card
    else:
        high.append(hand_tup)
    
# Sort the hands in each
five_kind.sort(reverse=True)
four_kind.sort(reverse=True)
full_house.sort(reverse=True)
three_kind.sort(reverse=True)
two_pair.sort(reverse=True)
one_pair.sort(reverse=True)
high.sort(reverse=True)

# Calculate total winnings
score = 0
for hand in five_kind:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in four_kind:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in full_house:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in three_kind:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in two_pair:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in one_pair:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in high:
    score += total_hands * hand[1]
    total_hands -= 1

print(score)

f.close()


# Part 2 -------------------------------------------

file_name = 'data.txt'
# file_name = 'data-test.txt'

f = open(file_name)

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high = []

total_hands = 0

for line in f:
    total_hands += 1
    line = line.strip()
    split_l = line.split()
    card_dict = {}
    hand = split_l[0]
    score = int(split_l[1])
    hand_l = []
    for card in hand:
        # Add the card to the hand list
        if card.isnumeric():
            hand_l.append(int(card))
        elif card == 'T':
            hand_l.append(10)
        elif card == 'J':
            hand_l.append(1)
        elif card == 'Q':
            hand_l.append(12)
        elif card == 'K':
            hand_l.append(13)
        else:
            hand_l.append(14)
        if card not in card_dict:
            card_dict.update({card:1})
        else:
            card_dict.update({card:(card_dict.get(card) + 1)})
    hand_tup = (hand_l, score)

    # !! at this point, we want to adjust how we treat J's. Always best to glom on to whatever the highest other count is.
    # First, remove the jacks from the dictionary, assuming we have less than 5
    if (len(card_dict) > 1) and 'J' in card_dict:
        jack_count = card_dict.get('J')
        card_dict.pop('J')
        # get the max remaining entry and add to that
        max_key = max(card_dict, key=card_dict.get)
        # add jacks to that key
        card_dict.update({max_key:(card_dict.get(max_key) + jack_count)})

    # Add to the appropriate list
    # 5 of a kind
    if len(card_dict) == 1:
        five_kind.append(hand_tup)
    # four of a kind or full house
    elif len(card_dict) == 2:
        if 4 in card_dict.values():
            four_kind.append(hand_tup)
        else:
            full_house.append(hand_tup)
    #three of a kind or two pair
    elif len(card_dict) == 3:
        if 3 in card_dict.values():
            three_kind.append(hand_tup)
        else:
            two_pair.append(hand_tup)
    # one pair
    elif len(card_dict) == 4:
        one_pair.append(hand_tup)
    # high card
    else:
        high.append(hand_tup)
    
# Sort the hands in each
five_kind.sort(reverse=True)
four_kind.sort(reverse=True)
full_house.sort(reverse=True)
three_kind.sort(reverse=True)
two_pair.sort(reverse=True)
one_pair.sort(reverse=True)
high.sort(reverse=True)

# Calculate total winnings
score = 0
for hand in five_kind:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in four_kind:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in full_house:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in three_kind:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in two_pair:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in one_pair:
    score += total_hands * hand[1]
    total_hands -= 1

for hand in high:
    score += total_hands * hand[1]
    total_hands -= 1

print(score)

f.close()