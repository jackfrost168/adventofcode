from collections import defaultdict


def check_part_number(positions, engine):
    is_part_number = False
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for (pos_i, pos_j) in positions:
        for (dir_i, dir_j) in directions:
            neighbor_i, neighbor_j = pos_i + dir_i, pos_j + dir_j
            if 0 <= neighbor_i <= len(engine) - 1 and 0 <= neighbor_j <= len(engine[0]) - 1:
                if engine[neighbor_i][neighbor_j] not in '0123456789.':
                    is_part_number = True
                    return is_part_number

    return is_part_number


def check_star(positions, engine):
    is_neighbor_star = False
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for (pos_i, pos_j) in positions:
        for (dir_i, dir_j) in directions:
            neighbor_i, neighbor_j = pos_i + dir_i, pos_j + dir_j
            if 0 <= neighbor_i <= len(engine) - 1 and 0 <= neighbor_j <= len(engine[0]) - 1:
                if engine[neighbor_i][neighbor_j] == '*':
                    is_neighbor_star = True
                    return is_neighbor_star, (neighbor_i, neighbor_j)

    return is_neighbor_star, False


def part1(engine):
    total = 0
    for i in range(len(engine)):
        j = 0
        num, pos = '', []
        while j < len(engine[i]):
            value = engine[i][j]
            if value in '0123456789':
                num += value
                pos.append((i, j))
            if (num != '' and value not in '0123456789') or (num != '' and j == len(engine[i])-1):
                is_part_number = check_part_number(pos, engine)
                if is_part_number == True:
                    total += int(num)
                num, pos = '', []
            j += 1

    return total


def part2(engine):
    gears = defaultdict(list)
    for i in range(len(engine)):
        j = 0
        num, pos = '', []
        while j < len(engine[i]):
            value = engine[i][j]
            if value in '0123456789':
                num += value
                pos.append((i, j))
            if (num != '' and value not in '0123456789') or (num != '' and j == len(engine[i])-1):
                is_neighbor_star, star_pos = check_star(pos, engine)
                if is_neighbor_star == True:
                    gears[star_pos].append(int(num))
                num, pos = '', []
            j += 1

    total = 0
    for key in gears.keys():
        if len(gears[key]) == 2:
            total += gears[key][0] * gears[key][1]

    return total


def main():
    with open("input/input3.txt", "r") as f:
        engine = [line.strip() for line in f.readlines()]

    print("part 1:", part1(engine[:]))
    print("part 2:", part2(engine[:]))


main()


# import itertools
# import math
# import re
# from collections import defaultdict
#
# with open("input/input3.txt") as f:
#     ls = f.read().strip().split("\n")
#
# box = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
# symbols = {
#     (i, j)
#     for i, l in enumerate(ls)
#     for j, x in enumerate(l)
#     if x != "." and not x.isdigit()
# }
#
# part_sum = 0
# parts_by_symbol = defaultdict(list)
#
# for i, l in enumerate(ls):
#     for match in re.finditer(r"\d+", l):
#         n = int(match.group(0))
#         boundary = {
#             (i + di, j + dj)
#             for di, dj in box
#             for j in range(match.start(), match.end())
#         }
#         if symbols & boundary:
#             part_sum += n
#         for symbol in symbols & boundary:
#             parts_by_symbol[symbol].append(n)
# # Part 1
# print(part_sum)
#
# print(sum(math.prod(v) for v in parts_by_symbol.values() if len(v) == 2))