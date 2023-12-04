import math


def part1(cards):
    total = 0
    for [win_nums, my_nums] in cards:
        winning_nums = set(win_nums) & set(my_nums)
        count = len(list(winning_nums))

        point = 1 * int(math.pow(2, count-1)) if count > 0 else 0

        total += point

    return total


def part2(cards):
    copies = [1] * len(cards)
    for i, [win_nums, my_nums] in enumerate(cards):
        winning_nums = set(win_nums) & set(my_nums)
        count = len(list(winning_nums))

        for j in range(i+1, i+count+1):
            copies[j] += 1 * copies[i]

    return sum(copies)


def main():
    with open("input/input4.txt", "r") as f:
        cards = []
        for line in f.readlines():
            line = line.strip().split(': ')
            win_and_my = line[1].split(' | ')
            win_nums = [int(num) for num in win_and_my[0].split()]
            my_nums = [int(num) for num in win_and_my[1].split()]
            cards.append([win_nums, my_nums])

    print("part 1:", part1(cards[:]))
    print("part 2:", part2(cards[:]))


main()
