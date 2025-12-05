def part1(pairs):
    pos = 50
    password = 0
    for pair in pairs:
        dir = pair[0]
        num = int(pair[1:])
        if dir == "R":
            pos += num
        elif dir == "L":
            pos -= num
        pos = pos % 100
        if pos == 0:
            password += 1

    return password

def part2(pairs):
    pos = 50
    password = 0
    for pair in pairs:

        dir = pair[0]
        num = int(pair[1:])

        if dir == "R":
            pos += num
            password += pos // 100
        elif dir == "L":
            if (pos - num % 100) <= 0 and pos != 0:
                password += 1
            password += num // 100
            pos -= num
        pos = pos % 100

    return password


def main():
    with open("input/input1.txt", "r") as f:
        inputs = [line.strip() for line in f.readlines()]
    print("part 1:", part1(inputs[:]))
    print("part 2:", part2(inputs[:]))

main()
