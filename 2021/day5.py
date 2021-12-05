def check_hori_or_vert(points):
    point1, point2 = points[0], points[1]
    if point1[0] == point2[0] or point1[1] == point2[1]:
        return 1
    else:
        return 0


def check_hori_or_vert_diag(points):
    point1, point2 = points[0], points[1]
    if point1[0] == point2[0] or point1[1] == point2[1]:
        return 1
    elif abs(point1[0] - point2[0]) == abs(point1[1] - point2[1]):
        return 1
    else:
        return 0


def part1(vents):
    appeared = {}
    for line in vents:
        if check_hori_or_vert(line):
            point1, point2 = line[0], line[1]
            if point1[0] == point2[0]:
                begin, end = min(point1[1], point2[1]), max(point1[1], point2[1])
                y = point1[0]
                for i in range(begin, end + 1):
                    if (i, y) not in appeared.keys():
                        appeared[(i, y)] = 1
                    else:
                        appeared[(i, y)] += 1
            elif point1[1] == point2[1]:
                begin, end = min(point1[0], point2[0]), max(point1[0], point2[0])
                x = point1[1]
                for i in range(begin, end + 1):
                    if (x, i) not in appeared.keys():
                        appeared[(x, i)] = 1
                    else:
                        appeared[(x, i)] += 1

    count = 0
    for key in appeared.keys():
        if appeared[key] >= 2:
            count += 1

    return count


def part2(vents):
    appeared = {}
    for line in vents:
        if check_hori_or_vert_diag(line):
            point1, point2 = line[0], line[1]
            if point1[0] == point2[0]:
                begin, end = min(point1[1], point2[1]), max(point1[1], point2[1])
                y = point1[0]
                for i in range(begin, end + 1):
                    if (i, y) not in appeared.keys():
                        appeared[(i, y)] = 1
                    else:
                        appeared[(i, y)] += 1

            elif point1[1] == point2[1]:
                begin, end = min(point1[0], point2[0]), max(point1[0], point2[0])
                x = point1[1]
                for i in range(begin, end + 1):
                    if (x, i) not in appeared.keys():
                        appeared[(x, i)] = 1
                    else:
                        appeared[(x, i)] += 1

            elif abs(point1[0] - point2[0]) == abs(point1[1] - point2[1]):
                if (point1[0] - point2[0]) == (point1[1] - point2[1]):
                    y, x = min(point1[0], point2[0]), min(point1[1], point2[1])
                    steps = abs(point1[0] - point2[0])
                    for i in range(steps + 1):
                        if (x + i, y + i) not in appeared.keys():
                            appeared[(x + i, y + i)] = 1
                        else:
                            appeared[(x + i, y + i)] += 1
                elif (point1[0] - point2[0]) == -1 * (point1[1] - point2[1]):
                    y, x = min(point1[0], point2[0]), max(point1[1], point2[1])
                    steps = abs(point1[1] - point2[1])
                    for i in range(steps + 1):
                        if (x - i, y + i) not in appeared.keys():
                            appeared[(x - i, y + i)] = 1
                        else:
                            appeared[(x - i, y + i)] += 1

    count = 0
    for key in appeared.keys():
        if appeared[key] >= 2:
            count += 1

    return count


def main():
    with open("input/input5.txt", "r") as f:  # open file
        f = f.readlines()  # read line, lines stores the txt file
    f = [points.strip().split(' -> ') for points in f]

    vents = []
    for line in f:
        points = []
        for point in line:
            point = point.split(',')
            points.append((int(point[0]), int(point[1])))
        vents.append(points)

    ans1 = part1(vents)
    print("part 1:", ans1)
    ans2 = part2(vents)
    print("part 2:", ans2)


main()
