def part1(groups):
    ans = 0
    for group in groups:
        yes_map = {}
        for person in group:
            for s in person:
                if s not in yes_map.keys():
                    yes_map[s] = 1
        ans = ans + len(yes_map.keys())
    return ans


def part2(groups):
    ans = 0
    for group in groups:
        yes_map = {}
        for person in group:
            for s in person:
                if s not in yes_map.keys():
                    yes_map[s] = 1
                else:
                    yes_map[s] += 1
        tmp_count = 0
        for key in yes_map.keys():
            if yes_map[key] == len(group):
                tmp_count += 1
        ans = ans + tmp_count
    return ans


def main():
    with open("input/input6.txt", "r") as f:
        lines = f.readlines()
        groups = []
        tmp = []
        for line in lines:
            line = line.strip('\n')
            if len(line) != 0:
                tmp.append(line[:])
            else:
                groups.append(tmp)
                tmp = []
        groups.append(tmp)

    ans1 = part1(groups)
    print('part1:', ans1)
    ans2 = part2(groups)
    print('part2:', ans2)


main()
