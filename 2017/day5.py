def part1(instructions):
    i = 0
    steps = 0
    while i < len(instructions):
        new_i = i + instructions[i]
        instructions[i] += 1
        i = new_i
        steps += 1
    return steps


def part2(instructions):
    i = 0
    steps = 0
    while i < len(instructions):
        new_i = i + instructions[i]
        if instructions[i] >= 3:
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i = new_i
        steps += 1
    return steps


def main():
    with open('input/input5.txt', 'r') as f:
        f = f.readlines()
    instructions = [int(num) for num in f]
    answer1 = part1(instructions[:])
    print('part1:', answer1)
    answer2 = part2(instructions[:])
    print('part2:', answer2)


main()
