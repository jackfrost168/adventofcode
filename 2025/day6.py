def part1(inputs):
    answer = 0
    n_rows = len(inputs)
    n_cols = len(inputs[0])
    for j in range(n_cols):
        value = int(inputs[0][j])
        for i in range(1, n_rows-1):
            if inputs[-1][j] == '+':
                value += int(inputs[i][j])
            elif inputs[-1][j] == "*":
                value *= int(inputs[i][j])
        answer += value

    return answer


def data_split(inputs, inputs2):
    n_rows = len(inputs)
    n_cols = len(inputs[0])
    max_n_set = []
    for j in range(n_cols):
        max_n_digit = 0
        for i in range(0, n_rows-1):
            value = inputs[i][j]
            if len(value) > max_n_digit:
                max_n_digit = len(value)
        max_n_set.append(max_n_digit)

    splited_data = []
    for line in inputs2:
        row_data = []
        i = 0
        for n_num in max_n_set:
            value = line[i: i+n_num]
            while len(value) < n_num:
                value = value + " "
            row_data.append(value)
            i += n_num + 1

        splited_data.append(row_data)

    return splited_data, max_n_set


def rotate_left(matrix):
    return [list(row) for row in zip(*matrix)][::-1]


def part2(inputs, inputs2):
    splited_data, max_n_set = data_split(inputs, inputs2)

    answer = 0
    n_rows, n_cols = len(inputs), len(inputs[0])
    for j in range(n_cols):
        values = []
        for i in range(0, n_rows-1):
            value = splited_data[i][j]
            values.append(list(value))
        new_values = rotate_left(values)

        value_seq = []
        for value in new_values:
            num = ""
            for digit in value:
                if digit != ' ':
                    num += digit
            value_seq.append(num)

        v = int(value_seq[0])
        n_nums = max_n_set[j]
        for i in range(1, n_nums):
            if inputs[-1][j] == '+':
                v += int(value_seq[i])
            elif inputs[-1][j] == "*":
                v *= int(value_seq[i])
        answer += v

    return answer


def main():
    with open("input/input6.txt", "r") as f:
        inputs = [line.strip() for line in f.readlines()]
        inputs = [line.split() for line in inputs]
    with open("input/input6.txt", "r") as f:
        inputs2 = f.read().split("\n")

    print("part 1:", part1(inputs[:]))
    print("part 2:", part2(inputs[:], inputs2[:]))

main()
