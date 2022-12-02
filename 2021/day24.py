def part1(instructions):
    x, y, z = 0, 0, 0
    for line in instructions:
        if line.startswith('inp'):
            w = range(9, 0, -1)
            continue
        if line.startswith('add'):
            line = line.split()



def main():
    with open('input/input24.txt', 'r') as f:
        instructions = f.read().splitlines()
    # instructions = []
    # for line in text:
    #     instructions.append(line.split())

    print("part 1:", part1(instructions))
    #print("part 2:", part2(steps))


main()