def part1(signal):
    for i, word in enumerate(signal):
        marker = {signal[i], signal[i+1], signal[i+2], signal[i+3]}

        if len(marker) == 4:
            return i + 4


def part2(signal):
    for i in range(len(signal)):
        marker = set()
        for j in range(14):
            marker.add(signal[i+j])

        if len(marker) == 14:
            return i + 14



def main():
    with open("input/input6.txt", "r") as f:  # open file
        signal = f.read()

    print("part 1:", part1(signal))
    print("part 2:", part2(signal))


main()
