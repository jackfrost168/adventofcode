def part1(sequence):
    position = [0, 0]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    dir_pos = 0
    for step in sequence:
        if step.startswith('R'):
            dir_pos = (dir_pos + 1) % 4
        else:
            dir_pos = (dir_pos - 1) % 4
        x, y = directions[dir_pos]
        position[0] += x * int(step[1:])
        position[1] += y * int(step[1:])
    return abs(position[0]) + abs(position[1])


def part2(sequence):
    position = [0, 0]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # up, right, down, left
    dir_pos = 0
    visited = set()
    visited.add((0, 0))
    for step in sequence:
        if step.startswith('R'):
            dir_pos = (dir_pos + 1) % 4
        else:
            dir_pos = (dir_pos - 1) % 4
        x, y = directions[dir_pos]

        for i in range(position[abs(y)], position[abs(y)] + int(step[1:])):
            position[abs(y)] += 1 * (x + y)
            if (position[0], position[1]) in visited:
                return abs(position[0]) + abs(position[1])
            visited.add((position[0], position[1]))


def main():
    with open("input/input1.txt", "r") as f:  # open file
        sequence = f.read().strip().split(' ')  # read line, lines stores the txt file

    sequence = [step.strip(',') for step in sequence]

    ans1 = part1(sequence[:])
    print("part 1:", ans1)
    ans2 = part2(sequence[:])
    print("part 2:", ans2)


main()
