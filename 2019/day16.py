def repeat_pattern(repeat):
    pattern = []
    base_pattern = [0, 1, 0, -1]
    for num in base_pattern:
        for _ in range(repeat+1):
            pattern.append(num)
    return pattern


def part1(signal):
    phase = 0
    while phase < 100:
        new_signal = []
        for repeat, ele in enumerate(signal):
            pattern = repeat_pattern(repeat)
            pattern_len = len(pattern)
            value = 0
            for i in range(len(signal)):
                value += signal[i] * pattern[(i+1) % pattern_len]
            value = abs(value) % 10
            new_signal.append(value)
        signal = new_signal
        phase += 1

    ans = [str(num) for num in signal[0:8]]
    ans = ''.join(ans)
    return int(ans)


def part2(signal):
    signal *= 10000
    offset = [str(s) for s in signal[0:7]]
    offset = ''.join(offset)
    offset = int(offset)

    for _ in range(100):
        for i in reversed(range(offset, len(signal) - 1)):
            signal[i] = (signal[i] + signal[i + 1]) % 10

    ans = [str(num) for num in signal[offset:offset + 8]]
    ans = ''.join(ans)
    return int(ans)


def main():
    with open('input/input16.txt', 'r') as f:
        signal = f.read().strip()
        signal = [int(num) for num in signal]

    ans1 = part1(signal)
    print('part1:', ans1)
    ans2 = part2(signal)
    print('part2:', ans2)


main()
