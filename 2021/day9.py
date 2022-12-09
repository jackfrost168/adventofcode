def check_lowest(heightmap, i, j):
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for d_x, d_y in direction:
        if 0 <= i+d_x <= len(heightmap)-1 and 0 <= j+d_y <= len(heightmap[0])-1:
            if heightmap[i][j] >= heightmap[i+d_x][j+d_y]:
                return False

    return True


def part1(heightmap):
    total_risk = 0
    for i, line in enumerate(heightmap):
        for j, num in enumerate(line):
            if check_lowest(heightmap, i, j):
                total_risk += heightmap[i][j] + 1

    return total_risk


def dfs(heightmap, i, j, mask):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d_x, d_y in direction:
        if 0 <= i+d_x <= len(heightmap)-1 and 0 <= j+d_y <= len(heightmap[0])-1:
            if heightmap[i+d_x][j+d_y] > heightmap[i][j] and heightmap[i+d_x][j+d_y] != 9:
                mask[i+d_x][j+d_y] = 1
                dfs(heightmap, i+d_x, j+d_y, mask)


def part2(heightmap):
    mask = [[0] * len(heightmap[0]) for i in range(len(heightmap))]

    basins = []
    for i, line in enumerate(heightmap):
        for j, num in enumerate(line):
            if check_lowest(heightmap, i, j):
                pre_length = sum(map(sum, mask))  # map(sum, a): [sum(i) for i in a]
                mask[i][j] = 1
                dfs(heightmap, i, j, mask)
                cur_length = sum(map(sum, mask))
                basins.append(cur_length - pre_length)

    basins = sorted(basins, reverse=True)

    return basins[0]*basins[1]*basins[2]


def main():
    with open("input/input9.txt", "r") as f:  # open file
        f = f.readlines()  # read line, lines stores the txt file
    heightmap = []
    for line in f:
        row = []
        for num in line.strip():
            row.append(int(num))
        heightmap.append(row)

    print("part 1:", part1(heightmap[:]))
    print("part 2:", part2(heightmap[:]))


main()
