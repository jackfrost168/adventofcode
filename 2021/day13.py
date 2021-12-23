def part1(paper, folds):
    axis, pos = folds[0]
    new_paper = set()
    if axis == 'x':
        for x, y in paper:
            if x <= pos:
                new_paper.add((x, y))
            elif x > pos:
                if (2*pos - x, y) not in new_paper:
                    new_paper.add((2*pos-x, y))
    elif axis == 'y':
        for x, y in paper:
            if y <= pos:
                new_paper.add((x, y))
            elif y > pos:
                if (x, 2*pos-y) not in new_paper:
                    new_paper.add((x, 2*pos-y))
    paper = new_paper.copy()

    return len(paper)


def part2(paper, folds):
    for axis, pos in folds:
        new_paper = set()
        if axis == 'x':
            for x, y in paper:
                if x <= pos:
                    new_paper.add((x, y))
                elif x > pos:
                    if (2*pos - x, y) not in new_paper:
                        new_paper.add((2*pos-x, y))
        elif axis == 'y':
            for x, y in paper:
                if y <= pos:
                    new_paper.add((x, y))
                elif y > pos:
                    if (x, 2*pos-y) not in new_paper:
                        new_paper.add((x, 2*pos-y))
        paper = new_paper.copy()

    max_x, max_y = 0, 0
    for x, y in paper:
        if x > max_x: max_x = x
        if y > max_y: max_y = y

    for i in range(0, max_y + 1):
        line = ''
        for j in range(0, max_x + 1):
            if ((j, i) not in paper):
                line = line + ' '
            else:
                line = line + '#'
        print(line)


def main():
    paper = set()
    folds = []
    part = 1
    with open("input/input13.txt", "r") as f:  # open file
        for line in f.read().splitlines():
            if len(line) == 0:
                part = 2
                continue

            if part == 1:
                line = line.split(',')
                paper.add((int(line[0]), int(line[1])))
            elif part == 2:
                line = line.split()
                axis = line[2].split('=')
                folds.append((axis[0], int(axis[1])))

    print("part 1:", part1(paper.copy(), folds[:]))
    print("part 2:")
    part2(paper.copy(), folds[:])


main()
