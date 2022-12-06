from collections import defaultdict
import copy


def part1(stacks, moves):
    for line in moves:
        for i in range(line[0]):
            crate = stacks[line[1]].pop()
            stacks[line[2]].append(crate)

    top = ''
    for i in range(len(stacks.keys())):
        top = top + stacks[i+1][-1]

    return top


def part2(stacks, moves):
    for line in moves:
        tmp = []
        for i in range(line[0]):
            crate = stacks[line[1]].pop()
            tmp.insert(0, crate)
        stacks[line[2]] = stacks[line[2]] + tmp

    top = ''
    for i in range(len(stacks.keys())):
        top = top + stacks[i+1][-1]

    return top


def main():
    with open("input/input5.txt", "r") as f:  # open file

        stacks = defaultdict(list)
        stack_info = True
        moves = []
        for line in f.readlines():

            if len(line.strip()) == 0:
                stack_info = False
                continue
            if stack_info:

                for i in range(0, len(line), 4):
                    if line[i+1] != ' ' and ord(line[i+1]) > 57:
                        stacks[i//4+1].insert(0, line[i+1])
            else:
                line = line.split()

                move = []
                for i, num in enumerate(line):
                    if i == 1 or i == 3 or i == 5:
                        move.append(int(num))
                moves.append(move)

    print("part 1:", part1(copy.deepcopy(stacks), moves))
    print("part 2:", part2(copy.deepcopy(stacks), moves))


main()
