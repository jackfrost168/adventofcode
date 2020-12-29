# search speed: set>dict>>list
def part2(changes):
    frequency = 0
    appeared = {0}
    while True:
        for f in changes:
            frequency = frequency + f
            if frequency not in appeared:
                appeared.add(frequency)
            else:
                return frequency


def main():
    with open("input/input1.txt", "r") as f:  # open file
        changes = [int(line.strip()) for line in f]

    ans1 = sum(changes)
    print('part 1:', ans1)
    ans2 = part2(changes)
    print('part 2:', ans2)


main()
