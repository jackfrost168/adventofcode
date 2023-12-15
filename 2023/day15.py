from collections import defaultdict


def HASH(seq):
    cur_value = 0
    for s in seq:
        cur_value += ord(s)
        cur_value = cur_value * 17
        cur_value = cur_value % 256

    return cur_value


def part2(sequence):
    boxes = defaultdict(dict)
    for seq in sequence:
        if '=' in seq:
            label, lens = seq.split('=')
            box_id = HASH(label)
            boxes[box_id][label] = int(lens)
        else:
            label = seq[:-1]
            box_id = HASH(label)
            boxes[box_id].pop(label, None)

    total = 0
    for key in boxes.keys():
        for (j, value) in enumerate(boxes[key].values()):
            total += (key + 1) * (j + 1) * value

    return total


def main():
    with open('input/input15.txt') as f:
        sequence = f.read().strip().split(',')

    print('part1:', sum(map(HASH, sequence)))
    print('part2:', part2(sequence[:]))

main()
