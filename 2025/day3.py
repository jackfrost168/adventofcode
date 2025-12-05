def part1(banks):
    answer = 0
    n_rows, n_cols = len(banks), len(banks[0])
    for line in banks:
        largest = 0
        for i in range(n_cols-1):
            for j in range(i+1, n_cols):
                value = int(line[i] + line[j])
                if value > largest:
                    largest = value
        answer += largest

    return answer

def part2(banks):
    answer = 0
    n_rows, n_cols = len(banks), len(banks[0])
    for line in banks:
        number = []
        pos = 0
        for nth_d in range(11, -1, -1):
            largest_digit = 0
            for i in range(pos, n_cols-nth_d):
                if int(line[i]) > int(largest_digit):
                    largest_digit = line[i]
                    largest_pos = i
            number.append([largest_digit, largest_pos])
            pos = largest_pos + 1

        value = ""
        for (digit, pos) in number:
            value = value + digit
        #print(value)
        answer += int(value)

    return answer


def main():
    with open("input/input3.txt", "r") as f:
        inputs = [line.strip() for line in f.readlines()]

    print("part 1:", part1(inputs[:]))
    print("part 2:", part2(inputs[:]))

main()
