def part1(lower_bound, upper_bound):
    ans = 0
    for i in range(lower_bound, upper_bound + 1):
        string = str(i)
        double_flag = 0
        increase_flag = 1
        for j in range(1, 6):
            if int(string[j]) == int(string[j-1]):
                double_flag = 1
            if int(string[j]) < int(string[j-1]):
                increase_flag = 0
                break
        if double_flag == 1 and increase_flag == 1:
            ans = ans + 1
    return ans


def part2(lower_bound, upper_bound):
    ans = 0
    for i in range(lower_bound, upper_bound + 1):
        string = str(i)
        double_flag = 0
        increase_flag = 1
        num_dict = {}
        for j in range(1, 6):
            if int(string[j]) == int(string[j-1]):
                if int(string[j]) not in num_dict.keys():
                    num_dict[int(string[j])] = 2
                else:
                    num_dict[int(string[j])] += 1
            if int(string[j]) < int(string[j-1]):
                increase_flag = 0
                break
        for key in num_dict.keys():
            if num_dict[key] == 2:
                double_flag = 1
        if double_flag == 1 and increase_flag == 1:
            ans = ans + 1
    return ans


def main():
    f = "264793-803935".split("-")

    lower_bound = int(f[0])
    upper_bound = int(f[1])

    ans1 = part1(lower_bound, upper_bound)
    print("part1:", ans1)
    ans2 = part2(lower_bound, upper_bound)
    print("part2:", ans2)


main()