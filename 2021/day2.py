def part1(commands):
    horizontal, depth = 0, 0

    for code, num in commands:
        X = int(num)
        if code == 'forward':
            horizontal += X
        if code == 'up':
            depth -= X
        if code == 'down':
            depth += X
    return horizontal * depth


def part2(commands):
    horizontal, depth, aim = 0, 0, 0

    for code, num in commands:
        X = int(num)
        if code == 'forward':
            horizontal += X
            depth += aim * X
        if code == 'up':
            aim -= X
        if code == 'down':
            aim += X

    return horizontal * depth


def main():
    with open("input/input2.txt", "r") as f:  # open file
        commands = [line.strip().split() for line in f.read().splitlines()]

    print("part 1:", part1(commands))
    print("part 2:", part2(commands))


main()
