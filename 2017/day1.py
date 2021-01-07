def part1(digits):
    captcha = 0
    for i in range(len(digits)):
        match_pos = (i + 1) % len(digits)
        if digits[i] == digits[match_pos]:
            captcha += int(digits[i])

    return captcha


def part2(digits):
    captcha = 0
    for i in range(len(digits)):
        match_pos = (i + len(digits)//2) % len(digits)
        if digits[i] == digits[match_pos]:
            captcha += int(digits[i])

    return captcha


def main():
    with open('input/input1.txt', 'r') as f:
        digits = f.read().strip()

    ans1 = part1(digits)
    print('part 1:', ans1)
    ans2 = part2(digits)
    print('part 2:', ans2)


main()
