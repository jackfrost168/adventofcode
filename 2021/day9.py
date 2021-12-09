def check_lowest(heightmap, i, j):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # if 1 <= i <= len(heightmap) - 2 and 1 <= j <= len(heightmap[0]) - 2:
    #     if heightmap[i][j] < heightmap[i-1][j] and \
    #         heightmap[i][j] < heightmap[i+1][j] and \
    #         heightmap[i][j] < heightmap[i][j-1] and \
    #         heightmap[i][j] < heightmap[i][j+1]:
    #         return True
    #
    #     elif i == 0 or i == len()
    num_low = 0
    count_neighbor = 0
    for d_x, d_y in dir:
        if  0 <= i + d_x <= len(heightmap) - 1 and 0 <= j + d_y <= len(heightmap[0]) - 1:
            count_neighbor += 1
            if heightmap[i][j] < heightmap[i+d_x][j+d_y]:
                num_low += 1

    if num_low == count_neighbor:
        return True
    else:
        return False


def part1(heightmap):
    total_risk = 0
    for i, line in enumerate(heightmap):
        for j, num in enumerate(line):
            if check_lowest(heightmap, i, j):
                total_risk += heightmap[i][j] + 1

    return total_risk


def dfs(heightmap, i, j, mask):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d_x, d_y in dir:
        if 0 <= i + d_x <= len(heightmap) - 1 and 0 <= j + d_y <= len(heightmap[0]) - 1:
            if heightmap[i+d_x][j+d_y] > heightmap[i][j] and mask[i+d_x][j+d_y] != 1 and heightmap[i+d_x][j+d_y] != 9:
                mask[i+d_x][j+d_y] = 1
                dfs(heightmap, i+d_x, j+d_y, mask)


def count_mask(mask):
    count = 0
    for line in mask:
        for i in line:
            count += i
    return count


def part2(heightmap):
    mask = []
    for i in range(len(heightmap)):
        row = []
        for j in range(len(heightmap[0])):
            row.append(0)
        mask.append(row)

    basins = []
    for i, line in enumerate(heightmap):
        for j, num in enumerate(line):
            if check_lowest(heightmap, i, j):

                pre_length = count_mask(mask)
                mask[i][j] = 1
                dfs(heightmap, i, j, mask)
                cur_length = count_mask(mask)
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

    ans1 = part1(heightmap[:])
    print("part 1:", ans1)
    ans2 = part2(heightmap[:])
    print("part 2:", ans2)


main()
