def Intcode(program_copy, input):
    program = program_copy[:]
    output = 0
    i = 0
    while i < len(program):
        instruction = str(program[i])
        while len(instruction) < 4:
            instruction = "0" + instruction
        epcode = int(instruction[2:])
        mode1 = int(instruction[1])
        mode2 = int(instruction[0])

        if epcode == 99:
            return output
        if epcode == 3 or epcode == 4:
            if mode1 == 0:
                pos1 = program[i + 1]
            else:
                pos1 = i + 1
        else:
            if mode1 == 0:
                pos1 = program[i + 1]
            else:
                pos1 = i + 1
            if mode2 == 0:
                pos2 = program[i + 2]
            else:
                pos2 = i + 2
            if epcode != 5 and epcode != 6:
                pos_output = program[i + 3]

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
            output = program[pos1]
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


def main():
    with open('input/input5.txt', 'r') as f:
        program = [int(s) for s in f.read().strip().split(',')]

    ans1 = Intcode(program, 1)
    print("answer1:", ans1)
    ans2 = Intcode(program, 5)
    print("answer2:", ans2)


main()