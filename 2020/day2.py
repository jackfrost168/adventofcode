def part1(passwords):
    valid = 0
    for line in passwords:
        lower_bound = int(line[0])
        upper_bound = int(line[1])
        target = line[2]
        string = line[3]
        count = string.count(target)
        if lower_bound <= count <= upper_bound:
            valid = valid + 1
    return valid


def part2(passwords):
    valid = 0
    for line in passwords:
        pos1 = int(line[0]) - 1
        pos2 = int(line[1]) - 1
        target = line[2]
        string = line[3]
        if (string[pos1] == target and string[pos2] != target) or\
            (string[pos1] != target and string[pos2] == target):
            valid = valid + 1
    return valid


def main():
    with open("input/input2.txt", "r") as f: # open file
        lines = f.readlines()  # read line, lines stores the txt file
        passwords = []  # [2, 9, 'g', 'jpxcgggzgsgngrhght']
        for line in lines:
            line = line.strip('\n').replace('-', ' ').replace(':', '').split(' ')
            passwords.append(line)

    ans1 = part1(passwords)
    print("part 1:", ans1)
    ans2 = part2(passwords)
    print("part 2:", ans2)


main()
