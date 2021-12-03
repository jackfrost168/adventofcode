def count_0_1(binary_numbers):
    count_0, count_1 = 0, 0
    for bit in binary_numbers:
        if bit == '1':
            count_1 += 1
        elif bit == '0':
            count_0 += 1
    return count_0, count_1


def get_col_binary(report, position):
    col_binary_number = ''
    for line in report:
        col_binary_number += line[position]

    return col_binary_number


def part1(report):
    gamma_rate, epsilon_rate = '', ''
    for i in range(len(report[0])):
        col_binary_number = get_col_binary(report, i)

        count_0, count_1 = count_0_1(col_binary_number)
        if count_0 > count_1:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate * epsilon_rate


def part2(report):

    def keep_binary_number(report, pos, bit_target):
        report_new = report[:]
        for line in report:
            if line[pos] != bit_target:
                report_new.remove(line)

        return report_new


    oxygen_rating, CO2_rating = report[:], report[:]

    for i in range(len(report[0])):
        # oxygen_rating
        col_binary_number = get_col_binary(oxygen_rating, i)

        count_0, count_1 = count_0_1(col_binary_number)
        if len(oxygen_rating) != 1:
            if count_0 <= count_1:
                oxygen_rating = keep_binary_number(oxygen_rating, i, '1')
            elif count_0 > count_1:
                oxygen_rating = keep_binary_number(oxygen_rating, i, '0')

        # CO2_rating
        col_binary_number = get_col_binary(CO2_rating, i)
        count_0, count_1 = count_0_1(col_binary_number)
        if len(CO2_rating) != 1:
            if count_0 <= count_1:
                CO2_rating = keep_binary_number(CO2_rating, i, '0')
            elif count_0 > count_1:
                CO2_rating = keep_binary_number(CO2_rating, i, '1')

    oxygen_rating = int(oxygen_rating[0], 2)
    CO2_rating = int(CO2_rating[0], 2)

    return  oxygen_rating * CO2_rating


def main():
    with open("input/input3.txt", "r") as f:  # open file
        f = f.readlines()  # read line, lines stores the txt file
        report = [line.strip() for line in f]

    ans1 = part1(report)
    print("part 1:", ans1)
    ans2 = part2(report)
    print("part 2:", ans2)


main()
