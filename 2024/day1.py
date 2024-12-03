from collections import defaultdict

def part1(pairs):
    left = [int(pair[0]) for pair in pairs]
    right = [int(pair[1]) for pair in pairs]
    left = sorted(left)
    right = sorted(right)

    total = 0
    for i, j in zip(left, right):
        total += abs(i - j)

    return total

def part2(pairs):
    left = [int(pair[0]) for pair in pairs]
    right = [int(pair[1]) for pair in pairs]
    right_dict = defaultdict(int)
    for num in right:
        right_dict[num] += 1

    total = 0
    for num in left:
        total += num * right_dict[num]

    return total


def main():
    with open("input/input1.txt", "r") as f:
        pairs = [line.strip().split() for line in f.readlines()]

    print("part 1:", part1(pairs))
    print("part 2:", part2(pairs))


main()
