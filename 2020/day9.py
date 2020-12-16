def part1(input):
    for i in range(25, len(input)):
        tmp = input[i-25: i]
        cur_num = False
        for t in tmp:
            if input[i] - t in tmp and input[i] - t != t:
                cur_num = True
                break

        if cur_num == False:
            return input[i]


def part2(input, target):
    for i in range(len(input)):
        tmp = input[i]
        for j in range(i+1, len(input)):
            tmp = tmp + input[j]
            if tmp == target:
                return max(input[i:j + 1])+min(input[i:j + 1])


def main():
    with open("input/input9.txt", "r") as f: # open file
        lines = f.readlines()  # read line, lines stores the txt file
        input = [int(line.strip()) for line in lines]

    ans1 = part1(input)
    print('part1:', ans1)
    ans2 = part2(input, ans1)
    print('part2:', ans2)


main()