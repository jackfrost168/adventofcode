def solution1(input):
    ans = 0
    for num in input:
        ans = ans + num // 3 - 2
    return ans


def solution2(input):
    ans = 0
    for num in input:
        while num > 5: #num must greater than 0
            num = num // 3 - 2
            ans = ans + num
    return ans


def main():
    with open("input/input1.txt", "r") as f: # open file
        f = f.readlines()  # read line, lines stores the txt file
        input = [int(line.strip()) for line in f]

    ans1 = solution1(input)
    print("part1:", ans1)
    ans2 = solution2(input)
    print("part2:", ans2)


main()