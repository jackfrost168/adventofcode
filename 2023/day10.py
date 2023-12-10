import re


def find_S(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'S':
                return i, j


def move(tile, pos_x, pos_y, dir, input):
    if tile == '|':
        if dir == 0:
            return input[pos_x-1][pos_y], pos_x-1, pos_y, 0
        else:
            return input[pos_x+1][pos_y], pos_x+1, pos_y, 2
    elif tile == '-':
        if dir == 1:
            return input[pos_x][pos_y-1], pos_x, pos_y-1, 1
        else:
            return input[pos_x][pos_y+1], pos_x, pos_y+1, 3
    elif tile == 'L':
        if dir == 2:
            return input[pos_x][pos_y + 1], pos_x, pos_y + 1, 3
        else:
            return input[pos_x - 1][pos_y], pos_x - 1, pos_y, 0
    elif tile == 'J':
        if dir == 2:
            return input[pos_x][pos_y - 1], pos_x, pos_y - 1, 1
        else:
            return input[pos_x - 1][pos_y], pos_x - 1, pos_y, 0
    elif tile == '7':
        if dir == 0:
            return input[pos_x][pos_y - 1], pos_x, pos_y - 1, 1
        else:
            return input[pos_x + 1][pos_y], pos_x + 1, pos_y, 2
    elif tile == 'F':
        if dir == 0:
            return input[pos_x][pos_y + 1], pos_x, pos_y + 1, 3
        else:
            return input[pos_x + 1][pos_y], pos_x + 1, pos_y, 2


def erase_not_loop(input, visited):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if (i, j) not in visited:
                input[i][j] = '.'

    return input


def count_area(input):
    ans = 0
    for row in input:
        interior = 0
        row = re.sub(r"F-*7|L-*J", "", "".join(row))
        row = re.sub(r"F-*J|L-*7", "|", row)

        for c in row:
            if c == "|":
                interior += 1
            if interior % 2 == 1 and c == ".":
                ans += 1

    return ans


def part(input):
    start_x, start_y = find_S(input)
    steps = 1
    tile, pos_x, pos_y, dir = input[start_x][start_y+1], start_x, start_y+1, 3  # start: F
    visited = set()
    visited.add((pos_x, pos_y))
    while tile != 'S':
        tile, pos_x, pos_y, dir = move(tile, pos_x, pos_y, dir, input)
        visited.add((pos_x, pos_y))
        steps += 1

    input = erase_not_loop(input, visited)
    area = count_area(input)

    return steps//2, area


def main():
    with open('input/input10.txt') as f:
        input = [list(line.strip()) for line in f.readlines()]

        farthest, area = part(input[:])
        print('part1:', farthest)
        print('part2:', area)


main()
