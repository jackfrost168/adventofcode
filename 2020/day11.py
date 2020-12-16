import copy

def neighbor_condition(input, i, j, direction):
    num_neighbors = 0
    occupied = 0
    empty_or_floor = 0
    for (x, y) in direction:
        new_i = i + x
        new_j = j + y
        if (new_i >= 0 and new_i < len(input)) and \
                (new_j) >= 0 and new_j < len(input[0]):
            num_neighbors += 1
            if input[new_i][new_j] == '.' or input[new_i][new_j] == 'L':
                empty_or_floor += 1
            else:
                occupied += 1
    return occupied, empty_or_floor, num_neighbors


def visual_condition(input, i, j, direction):
    num_neighbors = 0
    occupied = 0
    empty_or_floor = 0
    for (x, y) in direction:
        is_occupied = False
        is_empty = False
        new_i = i + x
        new_j = j + y
        if (new_i >= 0 and new_i < len(input)) and \
                (new_j >= 0 and new_j < len(input[0])):
            num_neighbors += 1
        while (new_i >= 0 and new_i < len(input)) and \
                new_j >= 0 and new_j < len(input[0]):
            if input[new_i][new_j] == '#':
                is_occupied = True
                break
            elif input[new_i][new_j] == 'L':
                is_empty = True
                break
            new_i = new_i + x
            new_j = new_j + y
        if is_occupied == True:
            occupied += 1
        if is_empty == True or (is_empty == False and is_occupied == False):
            empty_or_floor += 1

    return occupied, empty_or_floor, num_neighbors


def part1(input, direction):
    while True:
        change = 0
        tmp_input = copy.deepcopy(input)
        for i in range(len(input)):
            for j in range(len(input[0])):
                if tmp_input[i][j] == '.':
                    continue
                occupied, empty_or_floor, num_neighbors = neighbor_condition(tmp_input, i, j, direction)
                if tmp_input[i][j] == 'L':
                    if empty_or_floor == num_neighbors:
                        input[i][j] = '#'
                        change = change + 1
                elif tmp_input[i][j] == '#':
                    if occupied >= 4:
                        input[i][j] = 'L'
                        change = change + 1
        if change == 0:
            ans = 0
            for row in input:
                ans = ans + row.count('#')
            return ans


def part2(input, direction):
    while True:
        change = 0
        tmp_input = copy.deepcopy(input)
        for i in range(len(input)):
            for j in range(len(input[0])):
                if tmp_input[i][j] == '.':
                    continue
                occupied, empty_or_floor, num_neighbors = visual_condition(tmp_input, i, j, direction)
                if tmp_input[i][j] == 'L':
                    if occupied == 0:
                        input[i][j] = '#'
                        change = change + 1
                elif tmp_input[i][j] == '#':
                    if occupied >= 5:
                        input[i][j] = 'L'
                        change = change + 1

        if change == 0:
            ans = 0
            for row in input:
                ans = ans + row.count('#')
            return ans


def main():
    f = open("input/input11.txt", "r")  # open file
    lines = f.readlines()  # read line, lines stores the txt file
    input = [list(line.strip()) for line in lines]

    direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    input1 = copy.deepcopy(input)
    ans1 = part1(input1, direction)
    print('part1:', ans1)
    input2 = copy.deepcopy(input)
    ans2 = part2(input2, direction)
    print('part2:', ans2)

main()