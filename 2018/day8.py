total_values = 0


def part1(numbers, i):  # backorder, deep first search
    childs = numbers[i]
    entries = numbers[i+1]

    while childs != 0:
        i = part1(numbers, i+2)
        childs -= 1

    if childs == 0:
        global total_values
        total_values += sum(numbers[i + 2: i + 2 + entries])
        return i + entries


def part2(numbers, i):
    childs = numbers[i]
    entries = numbers[i+1]

    if childs == 0:
        value = sum(numbers[i + 2: i + 2 + entries])
        return value, i + entries

    values = []

    while childs != 0:
        value, i = part2(numbers, i+2)
        values.append(value)
        childs -= 1
        if childs == 0:
            sum_value = 0
            for j in range(i+2, i+2+entries):
                entry_pos = numbers[j]
                if entry_pos <= len(values):
                    sum_value += values[entry_pos-1]
            return sum_value, i+entries


def main():
    with open('input/input8.txt', 'r') as f:
        numbers = [int(num) for num in f.read().strip().split(' ')]

    _ = part1(numbers, 0)
    print('part 1:', total_values)
    ans2, _ = part2(numbers, 0)
    print('part 2:', ans2)


main()
