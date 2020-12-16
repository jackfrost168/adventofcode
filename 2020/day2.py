def part1(input):
    ans = 0
    for line in input:
        lower_bound = line[0]
        upper_bound = line[1]
        target = line[2]
        string = line[3]
        count = 0
        for word in string:
            if word == target:
                count = count + 1
        if count >= lower_bound and count <= upper_bound:
            ans = ans + 1
    return ans


def part2(input):
    ans = 0
    for line in input:
        pos1 = line[0]
        pos2 = line[1]
        target = line[2]
        string = line[3]
        if (string[pos1-1] == target and string[pos2-1] != target) or\
            (string[pos1-1] != target and string[pos2-1] == target):
            ans = ans + 1
    return ans


def main():
    with open("input/input2.txt", "r") as f: # open file
        lines = f.readlines()  # read line, lines stores the txt file
        input = []  # [2, 9, 'g', 'jpxcgggzgsgngrhght']
        for line in lines:
            line = line.strip('\n')
            line = line.split(" ")  # take away '\n'
            tmp = []
            r = line[0].split('-')
            tmp.append(int(r[0]))
            tmp.append((int(r[1])))
            tmp.append(line[1][0]) #single word
            tmp.append(line[2]) #string
            input.append(tmp)

    ans1 = part1(input)
    print("part1:", ans1)
    ans2 = part2(input)
    print("part2:", ans2)


main()