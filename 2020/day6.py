def part1(input):
    ans = 0
    for group in input:
        yes_map = {}
        for person in group:
            for s in person:
                if s not in yes_map.keys():
                    yes_map[s] = 1
        ans = ans + len(yes_map.keys())
    return ans


def part2(input):
    ans = 0
    for group in input:
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
    f = open("input6.txt", "r")  # open file
    lines = f.readlines()  # read line, lines stores the txt file
    input = []
    tmp = []
    for line in lines:
        line = line.strip('\n')  # take away '\n'
        if len(line) != 0:
            tmp.append(line[:])
        else:
            input.append(tmp)
            tmp = []
    input.append(tmp)

    ans1 = part1(input)
    print('part1:', ans1)
    ans2 = part2(input)
    print('part2:', ans2)


main()