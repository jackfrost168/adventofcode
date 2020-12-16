def part1(text):
    polymers = []
    for s in text:
        if len(polymers) == 0:
            polymers.append(s)
        else:
            if abs(ord(s)-ord(polymers[-1])) == 32:
                polymers.pop()
            else:
                polymers.append(s)
    return len(polymers)


def part2(text):
    ans = len(text)
    for i in range(65, 91):
        tmp_text = text.replace(chr(i), '').replace(chr(i+32), '')
        polymers = []
        for s in tmp_text:
            if len(polymers) == 0:
                polymers.append(s)
            else:
                if abs(ord(s) - ord(polymers[-1])) == 32:
                    polymers.pop()
                else:
                    polymers.append(s)
        if len(polymers) < ans:
            ans = len(polymers)
    return ans


def main():
    with open('input/input5.txt', 'r') as f:
        text = f.read().strip('\n')

    ans1 = part1(text)
    print('part1:', ans1)
    ans2 = part2(text)
    print('part2:', ans2)


main()