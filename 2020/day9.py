def part1(preamble):
    for i in range(25, len(preamble)):
        tmp_nums = preamble[i - 25: i]
        valid = False
        for num in tmp_nums:
            if preamble[i] - num in tmp_nums and preamble[i] - num != num:
                valid = True
                break

        if valid is False:
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
        preamble = [int(line.strip()) for line in f]

    ans1 = part1(preamble)
    print('part1:', ans1)
    ans2 = part2(preamble, ans1)
    print('part2:', ans2)


main()
