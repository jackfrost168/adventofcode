def move_north(rocks):
    for (i, line) in enumerate(rocks):
        for (j, rock) in enumerate(line):
            if rock == '#' or rock == '.':
                continue
            row = i
            while row > 0:
                if rocks[row][j] == 'O' and rocks[row-1][j] == '.':
                    rocks[row][j] = '.'
                    rocks[row-1][j] = 'O'
                    row = row - 1
                else:
                    break

    return rocks


def part1(rocks):
    rocks = move_north(rocks)

    total = 0
    for (i, line) in enumerate(rocks):
        count_O = line.count('O')
        total += (len(rocks) - i) * count_O

    return total


def part2(rocks):
    cycle = 0
    totals = []
    while cycle <1000000000:
        for i in range(4):
            rocks = move_north(rocks)
            rocks = list(map(list, zip(*(rocks[::-1]))))

        total = 0
        for (i, line) in enumerate(rocks):
            count_O = line.count('O')
            total += (len(rocks) - i) * count_O

        if cycle > 222 and total in totals:
            last_seen = 0
            for j in range(len(totals)-1, 0, -1):
                if totals[j] == total:
                    last_seen = j
                    interval = len(totals) - j
                    break

            pos = (1000000000-last_seen) % interval
            final_total = totals[last_seen+pos-1]

            return final_total

        totals.append(total)
        cycle += 1


def main():
    with open('input/input14.txt') as f:
        rocks = [list(line.strip()) for line in f.readlines()]

    print('part1:', part1(rocks[:]))
    print('part2:', part2(rocks[:]))

main()
