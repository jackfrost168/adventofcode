from collections import defaultdict


def part1(paper, folds):
    for axis, pos in folds:
        new_paper = defaultdict()
        if axis == 'x':
            for x, y in paper.keys():
                if x <= pos:
                    new_paper[(x, y)] = 1
                elif x > pos:
                    if (2*pos - x, y) not in new_paper.keys():
                        new_paper[(2*pos-x, y)] = 1
        elif axis == 'y':
            for x, y in paper.keys():
                if y <= pos:
                    new_paper[(x, y)] = 1
                elif y > pos:
                    if (x, 2*pos-y) not in new_paper.keys():
                        new_paper[(x, 2*pos-y)] = 1
        paper = new_paper.copy()
        print('length:', len(paper.keys()))
    return len(paper.keys())


def part2(paper, folds):
    for axis, pos in folds:
        new_paper = defaultdict()
        if axis == 'x':
            for x, y in paper.keys():
                if x <= pos:
                    new_paper[(x, y)] = 1
                elif x > pos:
                    if (2*pos - x, y) not in new_paper.keys():
                        new_paper[(2*pos-x, y)] = 1
        elif axis == 'y':
            for x, y in paper.keys():
                if y <= pos:
                    new_paper[(x, y)] = 1
                elif y > pos:
                    if (x, 2*pos-y) not in new_paper.keys():
                        new_paper[(x, 2*pos-y)] = 1
        paper = new_paper.copy()
        print('length:', len(paper.keys()))

    max_x, max_y = 0, 0
    for x, y in paper.keys():
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    for i in range(0, max_y + 1):
        line = ''
        for j in range(0, max_x + 1):
            if ((j, i) not in paper.keys()):
                line = line + ' '
            else:
                line = line + '#'
        print(line)





def main():
    paper = defaultdict(int)
    folds = []
    part = 1
    with open("input/input13.txt", "r") as f:  # open file
        for line in f.read().splitlines():
            if len(line) == 0:
                part = 2
                continue

            if part == 1:
                line = line.split(',')
                paper[(int(line[0]), int(line[1]))] = 1
            elif part == 2:
                line = line.split()
                axis = line[2].split('=')
                folds.append((axis[0], int(axis[1])))

    print(paper)
    print(folds)

    print("part 1:", part1(paper.copy(), folds[:]))
    print("part 2:")
    part2(paper.copy(), folds[:])


main()