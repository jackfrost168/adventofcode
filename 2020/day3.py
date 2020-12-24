def slope(map_grid, right, down):
    ans = 0
    i = 0
    j = 0
    while i < len(map_grid) - down:
        if j + right >= len(map_grid[0]):
            j = j + right - len(map_grid[0])
        else:
            j = j + right
        i = i + down
        if map_grid[i][j] == '#':
            ans = ans + 1
    return ans


def main():
    with open("input/input3.txt", "r") as f:
        lines = f.readlines()
        map_grid = [line.strip() for line in lines]

    ans1 = slope(map_grid, 3, 1)
    print("part1:", ans1)

    tmp1 = slope(map_grid, 1, 1)
    tmp2 = slope(map_grid, 3, 1)
    tmp3 = slope(map_grid, 5, 1)
    tmp4 = slope(map_grid, 7, 1)
    tmp5 = slope(map_grid, 1, 2)
    ans2 = tmp1*tmp2*tmp3*tmp4*tmp5
    print("part2:", ans2)


main()
