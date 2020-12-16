def slope(input, right, down):
    ans = 0
    i = 0
    j = 0
    while i < len(input) - down:
        if j + right >= len(input[0]):
            j = j + right - len(input[0])
        else:
            j = j + right
        i = i + down
        if input[i][j] == '#':
            ans = ans + 1
    return ans


def main():
    with open("input/input3.txt", "r") as f: # open file
        lines = f.readlines()  # read line, lines stores the txt file
        input = [line.strip() for line in lines]

    ans1 = slope(input, 3, 1)
    print("part1:", ans1)

    tmp1 = slope(input, 1, 1)
    tmp2 = slope(input, 3, 1)
    tmp3 = slope(input, 5, 1)
    tmp4 = slope(input, 7, 1)
    tmp5 = slope(input, 1, 2)
    ans2 = tmp1*tmp2*tmp3*tmp4*tmp5
    print("part2:", ans2)


main()