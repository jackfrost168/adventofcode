def Intcode(program, input):
    output = []
    i = 0
    relative_base = 0
    while i < len(program):
        instruction = str(program[i])
        while len(instruction) < 5:
            instruction = "0" + instruction
        epcode = int(instruction[3:])
        mode1 = int(instruction[2])
        mode2 = int(instruction[1])
        mode3 = int(instruction[0])

        if epcode == 99:
            return output

        if mode1 == 0:
            pos1 = program[i + 1]
        elif mode1 == 1:
            pos1 = i + 1
        else:
            pos1 = relative_base + program[i + 1]
        if mode2 == 0:
            pos2 = program[i + 2]
        elif mode2 == 1:
            pos2 = i + 2
        else:
            pos2 = relative_base + program[i + 2]
        if mode3 == 0:
            pos_output = program[i + 3]
        elif mode3 == 1:
            pos_output = i + 3
        else:
            pos_output = relative_base + program[i + 3]

        if epcode == 1:
            program[pos_output] = program[pos1] + program[pos2]
            i = i + 4
        elif epcode == 2:
            program[pos_output] = program[pos1] * program[pos2]
            i = i + 4
        elif epcode == 3:
            program[pos1] = input
            i = i + 2
        elif epcode == 4:
            output.append(program[pos1])
            i = i + 2
        elif epcode == 5:
            if program[pos1] != 0:
                i = program[pos2]
            else:
                i = i + 3
        elif epcode == 6:
            if program[pos1] == 0:
                i = program[pos2]
            else:
                i = i + 3
        elif epcode == 7:
            if program[pos1] < program[pos2]:
                program[pos_output] = 1
            else:
                program[pos_output] = 0
            i = i + 4
        elif epcode == 8:
            if program[pos1] == program[pos2]:
                program[pos_output] = 1
            else:
                program[pos_output] = 0
            i = i + 4
        elif epcode == 9:
            relative_base = relative_base + program[pos1]
            i = i + 2


def main():
    with open('input/input9.txt') as f:
        program = [int(s) for s in f.read().strip().split(',')]
    program += [0] * 5000

    ans1 = Intcode(program[:], 1)
    print("part 1:", ans1[0])
    ans2 = Intcode(program[:], 2)
    print("part 2:", ans2[0])

main()
