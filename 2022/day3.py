def part1(rucksacks):
    total = 0

    for line in rucksacks:
        first = list(line[0: len(line)//2])
        second = list(line[len(line)//2: len(line)])

        for letter in second:
            if letter in first:
                priority = ord(letter)
                if 97 <= priority <= 122:
                    priority = priority - 96
                else:
                    priority = priority - 38
                total += priority

                break

    return total


def part2(rucksacks):
    total = 0

    for i in range(0, len(rucksacks), 3):
        first = list(rucksacks[i])
        second = list(rucksacks[i+1])
        third = list(rucksacks[i+2])

        for letter in first:
            if letter in second and letter in third:
                priority = ord(letter)
                if 97 <= priority <= 122:
                    priority = priority - 96
                else:
                    priority = priority - 38
                total += priority

                break

    return total


def main():
    with open("input/input3.txt", "r") as f:  # open file
        rucksacks = [line.strip() for line in f.readlines()]

    print("part 1:", part1(rucksacks))
    print("part 2:", part2(rucksacks))


main()
