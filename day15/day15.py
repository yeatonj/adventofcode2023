# File for day 15 of AoC 2023
# Written by Joshua Yeaton on 12/18/2023

def run_hash(str_in):
    cur_val = 0
    for c in str_in:
        cur_val += ord(c)
        cur_val *= 17
        cur_val %= 256
    return cur_val

def parse_seq(seq):
    if '-' in seq:
        op = '-'
        label = seq[:-1]
        box = run_hash(label)
        foc_len = -1
    else:
        op = '='
        split_seq = seq.split('=')
        label = split_seq[0]
        box = run_hash(label)
        foc_len = int(split_seq[1])
    return (box, label, op, foc_len)

if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    f = open(file_name)
    line = f.readline()
    init_seqs = line.strip()
    init_seqs = line.split(',')
    total = 0
    for seq in init_seqs:
        total += run_hash(seq)

    print('Part 1 answer is: ' + str(total))

    f.close()

    # -------- Part 2
    boxes = []
    for i in range(256):
        boxes.append([])
    f = open(file_name)
    line = f.readline()
    init_seqs = line.strip()
    init_seqs = line.split(',')
    for seq in init_seqs:
        (box, label, op, foc_len) = parse_seq(seq)
        cur_box = boxes[box]
        if op == '-':
            for i in range(len(cur_box)):
                if cur_box[i][0] == label:
                    del cur_box[i]
                    break
        else: # op is =
            found = False
            for i in range(len(cur_box)):
                if cur_box[i][0] == label:
                    cur_box[i][1] = foc_len
                    found = True
                    break
            if not found:
                cur_box.append([label, foc_len])    
    
    total = 0
    for i in range(len(boxes)):
        box_num_mult = i + 1
        for j in range(len(boxes[i])):
            focal_length = boxes[i][j][1]
            slot_num = j + 1
            total += box_num_mult * slot_num * focal_length

    print('Part 2 answer: ' + str(total))

    

    f.close()
