def part1(fishes):
    for i in range(80):
        new_fishes = fishes[:]
        for i, timer in enumerate(new_fishes):
            if timer == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1

    return len(fishes)


def part2(fishes):
    fish2timer ={}
    for i in range(0, 9):
        fish2timer[i] = 0
    for fish in fishes:
        fish2timer[fish] += 1

    for i in range(256):
        num_zeros = fish2timer[0]
        for key in range(0, 8):
            if key == 6:
                fish2timer[key] = fish2timer[key + 1] + num_zeros
            else:
                fish2timer[key] = fish2timer[key + 1]
        fish2timer[8] = num_zeros

    count = 0
    for key in fish2timer.keys():
        count += fish2timer[key]

    return count


def main():
    with open("input/input6.txt", "r") as f:  # open file
        f = f.read().split(',')  # read line, lines stores the txt file
    fishes = [int(i) for i in f]

    ans1 = part1(fishes[:])
    print("part 1:", ans1)
    ans2 = part2(fishes[:])
    print("part 2:", ans2)


main()
