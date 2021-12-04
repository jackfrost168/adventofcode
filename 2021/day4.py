def check(board, num):
    x, y = -1, -1
    for i, line in enumerate(board):
        for j, n in enumerate(line):
            if n == num:
                x, y = i, j
    return x, y


def check_win(mask):
    for line in mask:
        if sum(line) == 5:
            return 1

    for j in range(len(mask[0])):
        if mask[0][j] + mask[1][j] + mask[2][j] + mask[3][j] + mask[4][j] == 5:
            return 1

    return 0


def compute_points(board, mask):
    unmarked_score = 0
    for line_mask, line_board in zip(mask, board):
        for m, b in zip(line_mask, line_board):
            if m == 0:
                unmarked_score += b

    return unmarked_score


import copy
def part1(numbers, boards):
    masks = []
    m = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(len(boards)):
        mm = copy.deepcopy(m[:])
        masks.append(mm)

    for num in numbers:
        for board, mask in zip(boards, masks):
            i, j = check(board, num)
            if i != -1 and j != -1:
                mask[i][j] = 1

            if check_win(mask):
                points = compute_points(board, mask)

                return points * num


def part2(numbers, boards):
    masks = []
    won = []
    last_score = 0
    m = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(len(boards)):
        mm = copy.deepcopy(m[:])
        masks.append(mm)

    for num in numbers:
        for board, mask in zip(boards, masks):
            if boards.index(board) in won:
                continue

            i, j = check(board, num)
            if i != -1 and j != -1:
                mask[i][j] = 1

            if check_win(mask):
                points = compute_points(board, mask)
                won.append(boards.index(board))
                last_score = points * num

    return  last_score


def main():
    with open("input/input4.txt", "r") as f:  # open file
        f = f.readlines()  # read line, lines stores the txt file
    numbers = [int(num) for num in f[0].strip().split(',')]
    boards, board = [], []

    for line in f[1:]:
        line = line.strip().split()
        if len(line) == 0 and board:
            boards.append(board)
            board = []
        elif len(line):
            line = [int(i) for i in line]
            board.append(line)
    boards.append(board)

    ans1 = part1(numbers, boards)
    print("part 1:", ans1)
    ans2 = part2(numbers, boards)
    print("part 2:", ans2)


main()
