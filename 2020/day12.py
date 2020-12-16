def part1(input):
    dirs = 'NESW'
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x = 0
    y = 0
    direction = 'E'

    for (action, value) in input:
        if action in dirs:
            ind = dirs.index(action)
            x = x + moves[ind][0] * value
            y = y + moves[ind][1] * value

        elif action in 'LR':
            if action == 'L':
                value = 360 - value
            turn = value // 90
            pos_dir = dirs.index(direction)
            pos_dir = (pos_dir + turn) % 4
            direction = dirs[pos_dir]

        elif action == 'F':
            ind = dirs.index(direction)
            x = x + moves[ind][0] * value
            y = y + moves[ind][1] * value

    return abs(x)+abs(y)


def part2(input):
    ship_x = 0
    ship_y = 0
    dirs = 'NESW'
    wp_x = -1
    wp_y = 10
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for (action, value) in input:
        if action in 'NESW':
            ind = dirs.index(action)
            wp_x = wp_x + moves[ind][0] * value
            wp_y = wp_y + moves[ind][1] * value

        elif action in 'LR':
            if action == 'L':
                value = 360 - value
            while value > 0:
                wp_x, wp_y = wp_y, -wp_x
                value = value - 90

        elif action == 'F':
            ship_x = ship_x + wp_x * value
            ship_y = ship_y + wp_y * value

    return abs(ship_x)+abs(ship_y)


def main():
    f = open("input/input12.txt", "r")  # open file
    lines = f.readlines()  # read line, lines stores the txt file
    input = []
    for line in lines:
        line = line.strip('\n')
        action = line[0]
        value = int(line[1:])
        input.append((action, value))

    ans1 = part1(input)
    print('part1:', ans1)
    ans2 = part2(input)
    print('part2:', ans2)


main()




# trash
# import math
# def part2(input):
#     ship_x = 0
#     ship_y = 0
#
#     wp_x = -1
#     wp_y = 10
#     direction = ['N', 'E']
#     dir = (('N','E'), ('E','S'), ('S','W'), ('W','N'))
#     for (action, value) in input:
#         if action == 'N':
#             wp_x = wp_x - value
#             if wp_x < ship_x and 'S' in direction:
#                 direction.remove('S')
#                 direction.append('N')
#         elif action == 'S':
#             wp_x = wp_x + value
#             if wp_x > ship_x and 'N' in direction:
#                 direction.remove('N')
#                 direction.append('S')
#         elif action == 'E':
#             wp_y = wp_y + value
#             if wp_y > ship_y and 'W' in direction:
#                 direction.remove('W')
#                 direction.append('E')
#         elif action == 'W':
#             wp_y = wp_y - value
#             if wp_y < ship_y and 'E' in direction:
#                 direction.remove('E')
#                 direction.append('W')
#         elif action == 'L':
#             turn = value // 90
#             pos_dir = 0
#             for i in range(len(dir)):
#                 if (direction[0] in dir[i]) and (direction[1] in dir[i]):
#                     pos_dir = i
#                     break
#             pos_dir = pos_dir - turn
#             pos_dir = pos_dir % 4
#             direction = list(dir[pos_dir])
#             angle = math.pi / (180 / value)
#             new_x = (wp_x - ship_x) * math.cos(angle) - (wp_y - ship_y) * math.sin(angle) + ship_x
#             new_y = (wp_x - ship_x) * math.sin(angle) + (wp_y - ship_y) * math.cos(angle) + ship_y
#             wp_x = int(round(new_x, 0))
#             wp_y = int(round(new_y, 0))
#         elif action == 'R':
#             turn = value // 90
#             #pos_dir = dir.index(direction)
#             pos_dir = 0
#             for i in range(len(dir)):
#                 if (direction[0] in dir[i]) and (direction[1] in dir[i]):
#                     pos_dir = i
#                     break
#             pos_dir = pos_dir + turn
#             pos_dir = pos_dir % 4
#             direction = list(dir[pos_dir])
#             angle = math.pi / (180 / value)
#             new_x = (wp_x - ship_x) * math.cos(angle) + (wp_y - ship_y) * math.sin(angle) + ship_x
#             new_y = (wp_y - ship_y) * math.cos(angle) - (wp_x - ship_x) * math.sin(angle) + ship_y
#             wp_x = int(round(new_x, 0))
#             wp_y = int(round(new_y, 0))
#         elif action == 'F':
#             tmp_x = abs(wp_x - ship_x)
#             tmp_y = abs(wp_y - ship_y)
#             if direction[0] == 'E':
#                 ship_y = ship_y + value * tmp_y
#                 wp_y = wp_y + value * tmp_y
#             elif direction[0] == 'W':
#                 ship_y = ship_y - value * tmp_y
#                 wp_y = wp_y - value * tmp_y
#             elif direction[0] == 'N':
#                 ship_x = ship_x - value * tmp_x
#                 wp_x = wp_x - value * tmp_x
#             elif direction[0] == 'S':
#                 ship_x = ship_x + value * tmp_x
#                 wp_x = wp_x + value * tmp_x
#             if direction[1] == 'E':
#                 ship_y = ship_y + value * tmp_y
#                 wp_y = wp_y + value * tmp_y
#             elif direction[1] == 'W':
#                 ship_y = ship_y - value * tmp_y
#                 wp_y = wp_y - value * tmp_y
#             elif direction[1] == 'N':
#                 ship_x = ship_x - value * tmp_x
#                 wp_x = wp_x - value * tmp_x
#             elif direction[1] == 'S':
#                 ship_x = ship_x + value * tmp_x
#                 wp_x = wp_x + value * tmp_x
#     return abs(ship_x)+abs(ship_y)