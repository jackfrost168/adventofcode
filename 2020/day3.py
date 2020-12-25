def slope(map_grid, right, down):
    trees = 0
    i, j = 0, 0
    height, width = len(map_grid), len(map_grid[0])
    while i < height - down:
        if j + right >= width:
            j = j + right - width
        else:
            j = j + right
        i = i + down
        if map_grid[i][j] == '#':
            trees = trees + 1
    return trees


def main():
    with open("input/input3.txt", "r") as f:
        lines = f.readlines()
        map_grid = [line.strip() for line in lines]

    ans1 = slope(map_grid, 3, 1)
    print('part 1:', ans1)

    tmp1 = slope(map_grid, 1, 1)
    tmp2 = slope(map_grid, 3, 1)
    tmp3 = slope(map_grid, 5, 1)
    tmp4 = slope(map_grid, 7, 1)
    tmp5 = slope(map_grid, 1, 2)
    ans2 = tmp1*tmp2*tmp3*tmp4*tmp5
    print('part 2:', ans2)


main()
