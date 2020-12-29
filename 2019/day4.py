def part1(lower_bound, upper_bound):
    ans = 0
    for i in range(lower_bound, upper_bound + 1):
        digits_string = str(i)
        double_flag = 0
        increase_flag = 1
        for j in range(1, 6):
            if int(digits_string[j]) == int(digits_string[j-1]):
                double_flag = 1
            if int(digits_string[j]) < int(digits_string[j-1]):
                increase_flag = 0
                break
        if double_flag == 1 and increase_flag == 1:
            ans = ans + 1
    return ans


def part2(lower_bound, upper_bound):
    ans = 0
    for i in range(lower_bound, upper_bound + 1):
        digits_string = str(i)
        double_flag = 0
        increase_flag = 1
        digit_dict = {}
        for j in range(1, 6):
            if int(digits_string[j]) == int(digits_string[j-1]):
                if int(digits_string[j]) not in digit_dict.keys():
                    digit_dict[int(digits_string[j])] = 2
                else:
                    digit_dict[int(digits_string[j])] += 1
            if int(digits_string[j]) < int(digits_string[j-1]):
                increase_flag = 0
                break
        for key in digit_dict.keys():
            if digit_dict[key] == 2:
                double_flag = 1
        if double_flag == 1 and increase_flag == 1:
            ans = ans + 1
    return ans


def main():
    with open('input/input4.txt', 'r') as f:
        f = f.read().strip().split("-")  # f = "264793-803935".split("-")

    lower_bound = int(f[0])
    upper_bound = int(f[1])

    ans1 = part1(lower_bound, upper_bound)
    print("part 1:", ans1)
    ans2 = part2(lower_bound, upper_bound)
    print("part 2:", ans2)


main()
