import copy

def part1(boot_code):
    accumulator = 0
    i = 0
    while i < len(boot_code.keys()):
        instruction = boot_code[i][0]
        argument = boot_code[i][1]
        if boot_code[i][2] == 1:
            break
        else:
            if instruction == 'acc':
                accumulator += argument
                boot_code[i][2] = 1
                i = i + 1
            elif instruction == 'nop':
                boot_code[i][2] = 1
                i = i + 1
            else:
                boot_code[i][2] = 1
                i = i + argument
    return accumulator


def part2(boot_code):
    for key in boot_code.keys():
        cur_boot_code = copy.deepcopy(boot_code)
        if boot_code[key][0] == 'nop':
            cur_boot_code[key][0] = 'jmp'
        elif boot_code[key][0] == 'jmp':
            cur_boot_code[key][0] = 'nop'
        else:
            continue

        accumulator = 0
        i = 0
        isloop = True
        while i < len(cur_boot_code.keys()):
            instruction = cur_boot_code[i][0]
            argument = cur_boot_code[i][1]
            if cur_boot_code[i][2] == 1:
                break
            else:
                if instruction == 'acc':
                    accumulator += argument
                    cur_boot_code[i][2] = 1
                    i = i + 1
                elif instruction == 'nop':
                    cur_boot_code[i][2] = 1
                    i = i + 1
                else:
                    cur_boot_code[i][2] = 1
                    i = i + argument
        if i >= len(cur_boot_code.keys()):
            isloop = False
        if isloop == False:
            return accumulator


def main():
    with open("input/input8.txt", "r") as f:
        lines = f.readlines()
        boot_code = {}
        for id, line in enumerate(lines):
            line = line.strip('\n').split(' ')
            boot_code[id] = [line[0], int(line[1]), 0]

    boot_code1 = copy.deepcopy(boot_code)
    ans1 = part1(boot_code1)
    print('part1:', ans1)
    boot_code2 = copy.deepcopy(boot_code)
    ans2 = part2(boot_code2)
    print('part2:', ans2)


main()
