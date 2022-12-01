def part1(calories):
    maximum, tmp_sum = 0, 0

    for i in calories:
        if i == '':
            if tmp_sum > maximum:
                maximum = tmp_sum
            tmp_sum = 0
        else:
            tmp_sum += int(i)

    return maximum


def part2(calories):
    carryings = []
    tmp_sum = 0

    for i in calories:
        if i == '':
            carryings.append(tmp_sum)
            tmp_sum = 0
        else:
            tmp_sum += int(i)

    carryings = sorted(carryings, reverse=True)

    return carryings[0] + carryings[1] + carryings[2]


def main():
    with open("input/input1.txt", "r") as f:  # open file
        Calories = [line.strip() for line in f.readlines()]

    print("part 1:", part1(Calories))
    print("part 2:", part2(Calories))


main()
