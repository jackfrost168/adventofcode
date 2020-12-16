import copy

def part1(input):
    accumulator = 0
    i = 0
    while i < len(input.keys()):
        instruction = input[i][0]
        argument = input[i][1]
        if input[i][2] == 1:
            break
        else:
            if instruction == 'acc':
                accumulator += argument
                input[i][2] = 1
                i = i + 1
            elif instruction == 'nop':
                input[i][2] = 1
                i = i + 1
            else:
                input[i][2] = 1
                i = i + argument
    return accumulator


def part2(input):
    for key in input.keys():
        cur_input = copy.deepcopy(input)
        if input[key][0] == 'nop':
            cur_input[key][0] = 'jmp'
        elif input[key][0] == 'jmp':
            cur_input[key][0] = 'nop'
        else:
            continue

        accumulator = 0
        i = 0
        isloop = True
        while i < len(cur_input.keys()):
            instruction = cur_input[i][0]
            argument = cur_input[i][1]
            if cur_input[i][2] == 1:
                break
            else:
                if instruction == 'acc':
                    accumulator += argument
                    cur_input[i][2] = 1
                    i = i + 1
                elif instruction == 'nop':
                    cur_input[i][2] = 1
                    i = i + 1
                else:
                    cur_input[i][2] = 1
                    i = i + argument
        if i >= len(cur_input.keys()):
            isloop = False
        if isloop == False:
            return accumulator


def main():
    f = open("input/input8.txt", "r")  # open file
    lines = f.readlines()  # read line, lines stores the txt file
    input = {}
    for id, line in enumerate(lines):
        line = line.strip('\n')  # take away '\n'
        line = line.split(' ')
        input[id] = [line[0], int(line[1]), 0]

    input1 = copy.deepcopy(input)
    ans1 = part1(input1)
    print('part1:', ans1)
    input2 = copy.deepcopy(input)
    ans2 = part2(input2)
    print('part2:', ans2)


main()