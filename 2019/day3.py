def route(line):
    i = 0
    j = 0
    path = {(0,0)}
    for step in line:
        direction = step[0]
        num = int(step[1:])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        ind = 'RLUD'.index(direction)

        for k in range(1, num+1):
            i = i + dirs[ind][0]
            j = j + dirs[ind][1]
            path.add((i, j))

    return path


def part1(path1, path2):
    ans = 100000
    for inter in path1:
        if inter in path2:
            if (abs(inter[0]) + abs(inter[1]) < ans) and (inter[0] != 0 and inter[1] != 0):
                ans = abs(inter[0]) + abs(inter[1])
    return ans


def path_length(line1, intersection):
    i = 0
    j = 0
    length = 0
    for step in line1:
        direction = step[0]
        num = int(step[1:])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        ind = 'RLUD'.index(direction)

        for k in range(1, num+1):
            length += 1
            i = i + dirs[ind][0]
            j = j + dirs[ind][1]
            if i == intersection[0] and j == intersection[1]:
                return length


def part2(path1, path2, line1, line2):
    ans = 1000000
    for inter in path1:
        if inter in path2:
            if (abs(inter[0]) + abs(inter[1]) < ans) and (inter[0] != 0 and inter[1] != 0):
                length1 = path_length(line1, inter)
                length2 = path_length(line2, inter)
                if length1 + length2 < ans:
                    ans = length1 + length2
    return ans


def main():
    with open("input/input3.txt", "r") as f: # open file
        lines = f.readlines()  # read line, lines stores the txt file

    line1 = lines[0].strip().split(',')
    line2 = lines[1].strip().split(',')

    path1 = route(line1)
    path2 = route(line2)

    ans1 = part1(path1, path2)
    print('part1:', ans1)
    ans2 = part2(path1, path2, line1, line2)
    print('part2:', ans2)


main()



