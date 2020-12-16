#search speed: set>dict>>list
def part2(input):
    frequency = 0
    appeared = {0}
    while True:
        for f in input:
            frequency = frequency + f
            if frequency not in appeared:
                appeared.add(frequency)
            else:
                return frequency


def main():
    f = open("input/input1.txt", "r")  # open file
    lines = f.readlines()  # read line, lines stores the txt file
    input = [int(line.strip()) for line in lines]

    ans1 = sum(input)
    print('part1:', ans1)
    ans2 = part2(input)
    print('part2:', ans2)


main()