from typing import List


def part1(instructions):
    code = ''
    x, y = 1, 1
    directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    for ins in instructions:
        for s in ins:
            dir_x, dir_y = directions[s]
            if 0 <= x + dir_x <= 2 and 0 <= y + dir_y <= 2:
                x += dir_x
                y += dir_y
        button = str(x * 3 + y + 1)
        code += button
    return code


def part2(instructions):
    code = ''
    x, y = 1, 1
    directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    position = {(0, 2): '1', (1, 1): '2', (1, 2): '3', (1, 3): '4',
                (2, 0): '5', (2, 1): '6', (2, 2): '7', (2, 3): '8',
                (2, 4): '9', (3, 1): 'A', (3, 2): 'B', (3, 3): 'C', (4, 2): 'D'}
    for ins in instructions:
        for s in ins:
            dir_x, dir_y = directions[s]
            if (x + dir_x, y + dir_y) in position.keys():
                x += dir_x
                y += dir_y
        button = position[(x, y)]
        code += button
    return code


def main():
    with open("input/input2.txt", "r") as f:  # open file
        instructions: List[str] = f.readlines()  # read line, lines stores the txt file

    instructions = [ins.strip() for ins in instructions]
    ans1 = part1(instructions[:])
    print("part 1:", ans1)
    ans2 = part2(instructions[:])
    print("part 2:", ans2)


main()
