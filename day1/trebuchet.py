# File for day 1 of AoC 2023
# Written by Joshua Yeaton on 12/1/2023

def find_first_num(line_of_text):
    for i in range(len(line_of_text)):
        if line_of_text[i] in nums:
            return line_of_text[i]
        elif line_of_text[i] == "z":
            if line_of_text[i:i+4] == "zero":
                return "0"
        elif line_of_text[i] == "o":
            if line_of_text[i:i+3] == "one":
                return "1"
        elif line_of_text[i] == "t":
            if line_of_text[i:i+3] == "two":
                return "2"
            elif line_of_text[i:i+5] == "three":
                return "3"
        elif line_of_text[i] == "f":
            if line_of_text[i:i+4] == "four":
                return "4"
            elif line_of_text[i:i+4] == "five":
                return "5"
        elif line_of_text[i] == "s":
            if line_of_text[i:i+3] == "six":
                return "6"
            elif line_of_text[i:i+5] == "seven":
                return "7"
        elif line_of_text[i] == "e":
            if line_of_text[i:i+5] == "eight":
                return "8"
        elif line_of_text[i] == "n":
            if line_of_text[i:i+4] == "nine":
                return "9"
        
        
def find_last_num(line_of_text):
    reversed_line = line_of_text[::-1]
    for i in range(len(reversed_line)):
        if reversed_line[i] in nums:
            return reversed_line[i]
        elif reversed_line[i] == "o":
            if reversed_line[i:i+4] == "orez":
                return '0'
            elif reversed_line[i:i+3] == "owt":
                return '2'
        elif reversed_line[i] == "e":
            if reversed_line[i:i+3] == "eno":
                return '1'
            elif reversed_line[i:i+5] == "eerht":
                return '3'
            elif reversed_line[i:i+4] == "evif":
                return '5'
            elif reversed_line[i:i+4] == "enin":
                return '9'
        elif reversed_line[i] == "r":
            if reversed_line[i:i+4] == "ruof":
                return '4'
        elif reversed_line[i] == "x":
            if reversed_line[i:i+3] == "xis":
                return '6'
        elif reversed_line[i] == "n":
            if reversed_line[i:i+5] == "neves":
                return '7'
        elif reversed_line[i] == "t":
            if reversed_line[i:i+5] == "thgie":
                return '8'




data = open("data.txt")
# data = open("data-test.txt")
# data = open("data-test-2.txt")

nums = "0123456789"

total = 0

for line in data:
    c_initial = find_first_num(line)
    c_final = find_last_num(line)
    total_c = c_initial + c_final
    print(total_c)
    total += int(total_c)

print("Total is : {}".format(total))