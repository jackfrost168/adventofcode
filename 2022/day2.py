def win_score1(A, B):
    if A == 'A':
        if B == 'X':
            return 3
        elif B == 'Y':
            return 6
        else:
            return 0
    elif A == 'B':
        if B == 'X':
            return 0
        elif B == 'Y':
            return 3
        else:
            return 6
    else:
        if B == 'X':
            return 6
        elif B == 'Y':
            return 0
        else:
            return 3


def part1(strategy):
    total = 0
    for line in strategy:
        if line[1] == 'X':
            score = 1
        elif line[1] == 'Y':
            score = 2
        else:
            score = 3
        score += win_score1(line[0], line[1])
        total += score

    return total


def win_score2(A, B):
    if A == 'A':
        if B == 'X':
            return 3
        elif B == 'Y':
            return 1
        else:
            return 2
    elif A == 'B':
        if B == 'X':
            return 1
        elif B == 'Y':
            return 2
        else:
            return 3
    else:
        if B == 'X':
            return 2
        elif B == 'Y':
            return 3
        else:
            return 1


def part2(strategy):
    total = 0
    for line in strategy:
        if line[1] == 'X':
            score = 0
        elif line[1] == 'Y':
            score = 3
        else:
            score = 6
        score += win_score2(line[0], line[1])
        total += score

    return total


def main():
    with open("input/input2.txt", "r") as f:  # open file
        strategy = [line.strip().split() for line in f.readlines()]

    print("part 1:", part1(strategy))
    print("part 2:", part2(strategy))


main()
