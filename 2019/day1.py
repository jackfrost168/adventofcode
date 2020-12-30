def solution1(masses):
    ans = 0
    for num in masses:
        ans = ans + num // 3 - 2
    return ans


def solution2(masses):
    ans = 0
    for num in masses:
        while num > 5:
            num = num // 3 - 2
            ans = ans + num
    return ans


def main():
    with open("input/input1.txt", "r") as f:  # open file
        masses = [int(line.strip()) for line in f]

    ans1 = solution1(masses)
    print("part 1:", ans1)
    ans2 = solution2(masses)
    print("part 2:", ans2)


main()
