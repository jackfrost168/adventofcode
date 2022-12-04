def part1(assignments):
    overlaps = 0

    for line in assignments:

        first = [int(i) for i in line[0].split('-')]
        second = [int(i) for i in line[1].split('-')]

        if (first[0] <= second[0] and first[1] >= second[1]) or \
            (first[0] >= second[0] and first[1] <= second[1]):
            overlaps += 1

    return overlaps


def part2(assignments):
    overlaps = 0

    for line in assignments:
        first = [int(i) for i in line[0].split('-')]
        second = [int(i) for i in line[1].split('-')]

        if not (first[0] > second[1] or first[1] < second[0]):
            overlaps += 1

    return overlaps


def main():
    with open("input/input4.txt", "r") as f:  # open file
        assignments = [line.strip().split(',') for line in f.readlines()]

    print("part 1:", part1(assignments))
    print("part 2:", part2(assignments))


main()
