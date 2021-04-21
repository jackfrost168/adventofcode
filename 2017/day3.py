def part1(square):
    root = int(pow(square, 0.5))
    if root % 2 == 1:
        root = root + 2
    elif root % 2 == 0:
        root = root + 1
    right_down = root * root
    left_up = right_down - (root - 1) * 2
    right_up = left_up - (root - 1)
    left_down = right_down - (root - 1)

    d = 0
    if left_up >= square >= right_up:
        mid = (left_up + right_up) // 2
        d = abs(square - mid)
    elif left_down <= square <= right_down:
        mid = (left_down + right_down) // 2
        d = abs(square - mid)
    elif left_up < square < left_down:
        mid = (left_up + left_down) // 2
        d = abs(square - mid)
    elif right_up > square:
        mid = right_up - (root - 1) // 2
        d = abs(square - mid)

    manhattan_d = d + (root - 1) // 2
    return manhattan_d


def count_neighbor(grid, i, j, seq):
    total = 0
    for m in [-1, 0, 1]:
        for n in [-1, 0, 1]:
            if m == n == 0:
                continue
            if 0 <= i+m < len(grid) and 0 <= j+n < len(grid):
                total += grid[i+m][j+n]
    seq.append(total)
    return total


def part2(square):
    center = 5
    grid = [[0 for row in range(center*2+1)] for col in range(center*2+1)]
    i, j = center, center
    grid[i][j] = 1
    layer = 1
    seq = [grid[i][j]]
    while layer <= center:
        j = j + 1
        grid[i][j] = count_neighbor(grid, i, j, seq)
        while i > center - layer:
            i = i - 1
            grid[i][j] = count_neighbor(grid, i, j, seq)
        while j > center - layer:
            j = j - 1
            grid[i][j] = count_neighbor(grid, i, j, seq)
        while i < center + layer:
            i = i + 1
            grid[i][j] = count_neighbor(grid, i, j, seq)
        while j < center + layer:
            j = j + 1
            grid[i][j] = count_neighbor(grid, i, j, seq)
        layer += 1

    for i in range(len(seq)):
        if seq[i] > square:
            return seq[i]


def main():
    with open('input/input3.txt', 'r') as f:
        square = int(f.read().strip())
    answer1 = part1(square)
    print('part1:', answer1)
    answer2 = part2(square)
    print('part2:', answer2)


main()
