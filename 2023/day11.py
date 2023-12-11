def part(input, larger=2):
    rows, cols = set(), set()
    for j in range(len(input[0])):
        col_empty = True
        for i in range(len(input)):
            if input[i].count('.') == len(input[i]):
                rows.add(i)
            if input[i][j] == '#':
                col_empty = False
                break
        if col_empty == True:
            cols.add(j)

    galaxies = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '#':
                galaxies.append((i, j))

    total = 0
    for i in range(len(galaxies)):
        for j in range(i):
            exlarge_row = 0
            for row in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])):
                if row in rows:
                    exlarge_row += 1
            exlarge_col = 0
            for col in range(min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])):
                if col in cols:
                    exlarge_col += 1

            distance = abs(galaxies[i][0]-galaxies[j][0])+exlarge_row*(larger-1) + abs(galaxies[i][1]-galaxies[j][1])+exlarge_col*(larger-1)
            total += distance

    return total


def main():
    with open('input\input11.txt') as f:
        input = [list(line.strip()) for line in f.readlines()]

        print('part1:', part(input[:], larger=2))
        print('part2:', part(input[:], larger=1000000))


main()
