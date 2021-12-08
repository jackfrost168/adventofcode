def part1(digit_out):
    count_1478 = 0
    for line in digit_out:
        for signal in line:
            if len(signal) == 2 or len(signal) == 3 or len(signal) == 4 or len(signal) == 7:
                count_1478 += 1

    return count_1478


def count_contains(signal, mask):
    count = 0
    for s in signal:
        if s in mask:
            count += 1

    return count


def part2(signals, digit_out):

    total_value = 0
    for signal, digit in zip(signals, digit_out):

        for s in signal:
            if len(s) == 2: one = s
            if len(s) == 4: four = s

        numstr = ''
        for d in digit:
            if len(d) == 2: numstr += '1'
            elif len(d) == 3: numstr += '7'
            elif len(d) == 4: numstr += '4'
            elif len(d) == 7: numstr += '8'
            elif len(d) == 5:
                if count_contains(d, one) == 2: numstr += '3'
                elif count_contains(d, four) == 2: numstr += '2'
                else: numstr += '5'
            else:
                if count_contains(d, four) == 4: numstr += '9'
                elif count_contains(d, one) == 2: numstr += '0'
                else: numstr += '6'

        total_value += int(numstr)

    return total_value


def main():
    with open("input/input8.txt", "r") as f:  # open file
        f = f.readlines()  # read line, lines stores the txt file

    f = [line.strip().split(' | ') for line in f]
    signals = [line[0].split() for line in f]
    digit_out = [line[1].split() for line in f]

    ans1 = part1(digit_out[:])
    print("part 1:", ans1)
    ans2 = part2(signals[:], digit_out[:])
    print("part 2:", ans2)


main()
