import copy

def neighbor_condition(seat_layout, i, j, direction):
    num_neighbors = 0
    occupied = 0
    empty_or_floor = 0
    for (x, y) in direction:
        new_i = i + x
        new_j = j + y
        if 0 <= new_i < len(seat_layout) and 0 <= new_j < len(seat_layout[0]):
            num_neighbors += 1
            if seat_layout[new_i][new_j] == '.' or seat_layout[new_i][new_j] == 'L':
                empty_or_floor += 1
            else:
                occupied += 1
    return occupied, empty_or_floor, num_neighbors


def visual_condition(seat_layout, i, j, direction):
    num_neighbors = 0
    occupied = 0
    empty_or_floor = 0
    for (x, y) in direction:
        is_occupied = False
        is_empty = False
        new_i = i + x
        new_j = j + y
        if 0 <= new_i < len(seat_layout) and 0 <= new_j < len(seat_layout[0]):
            num_neighbors += 1
        while 0 <= new_i < len(seat_layout) and 0 <= new_j < len(seat_layout[0]):
            if seat_layout[new_i][new_j] == '#':
                is_occupied = True
                break
            elif seat_layout[new_i][new_j] == 'L':
                is_empty = True
                break
            new_i = new_i + x
            new_j = new_j + y
        if is_occupied:
            occupied += 1
        if is_empty is True or (is_empty is False and is_occupied is False):
            empty_or_floor += 1

    return occupied, empty_or_floor, num_neighbors


def part1(seat_layout, direction):
    while True:
        change = 0
        tmp_input = copy.deepcopy(seat_layout)
        for i in range(len(seat_layout)):
            for j in range(len(seat_layout[0])):
                if tmp_input[i][j] == '.':
                    continue
                occupied, empty_or_floor, num_neighbors = neighbor_condition(tmp_input, i, j, direction)
                if tmp_input[i][j] == 'L':
                    if empty_or_floor == num_neighbors:
                        seat_layout[i][j] = '#'
                        change = change + 1
                elif tmp_input[i][j] == '#':
                    if occupied >= 4:
                        seat_layout[i][j] = 'L'
                        change = change + 1
        if change == 0:
            ans = 0
            for row in seat_layout:
                ans = ans + row.count('#')
            return ans


def part2(seat_layout, direction):
    while True:
        change = 0
        tmp_input = copy.deepcopy(seat_layout)
        for i in range(len(seat_layout)):
            for j in range(len(seat_layout[0])):
                if tmp_input[i][j] == '.':
                    continue
                occupied, empty_or_floor, num_neighbors = visual_condition(tmp_input, i, j, direction)
                if tmp_input[i][j] == 'L':
                    if occupied == 0:
                        seat_layout[i][j] = '#'
                        change = change + 1
                elif tmp_input[i][j] == '#':
                    if occupied >= 5:
                        seat_layout[i][j] = 'L'
                        change = change + 1

        if change == 0:
            ans = 0
            for row in seat_layout:
                ans = ans + row.count('#')
            return ans


def main():
    with open("input/input11.txt", "r") as f:
        lines = f.readlines()
        seat_layout = [list(line.strip()) for line in lines]

    direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    seat_layout1 = copy.deepcopy(seat_layout)
    ans1 = part1(seat_layout1, direction)
    print('part1:', ans1)
    seat_layout2 = copy.deepcopy(seat_layout)
    ans2 = part2(seat_layout2, direction)
    print('part2:', ans2)


main()
