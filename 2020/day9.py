def part1(preamble):
    for i in range(25, len(preamble)):
        tmp = preamble[i - 25: i]
        cur_num = False
        for t in tmp:
            if preamble[i] - t in tmp and preamble[i] - t != t:
                cur_num = True
                break

        if cur_num == False:
            return preamble[i]


def part2(preamble, target):
    for i in range(len(preamble)):
        tmp = preamble[i]
        for j in range(i+1, len(preamble)):
            tmp = tmp + preamble[j]
            if tmp == target:
                return max(preamble[i:j + 1]) + min(preamble[i:j + 1])


def main():
    with open("input/input9.txt", "r") as f:
        lines = f.readlines()
        preamble = [int(line.strip()) for line in lines]

    ans1 = part1(preamble)
    print('part1:', ans1)
    ans2 = part2(preamble, ans1)
    print('part2:', ans2)


main()
