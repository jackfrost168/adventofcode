def part(history, add_last=True):
    total = 0
    for line in history:
        is_not_zeros = True
        first_nums, last_nums = [], []
        while is_not_zeros:
            difference = [line[i+1] - line[i] for i in range(len(line)-1)]
            first_nums.append(line[0])
            last_nums.append(line[-1])
            line = difference[:]

            if difference.count(0) == len(difference):
                is_not_zeros = False

        if add_last == True:
            total += sum(last_nums)
        else:
            first_nums = first_nums[::-1]
            value = first_nums[0]
            for num in first_nums[1:]:
                value = num - value
            total += value

    return total


def main():
    with open('input/input9.txt') as f:
        history = [list(map(int, line.strip().split())) for line in f.readlines()]

        print('part1:', part(history[:], add_last=True))
        print('part2:', part(history[:], add_last=False))


main()
