def part1(monkeys):
    #items_updated = [[] * len(monkeys)]
    times = [0] * len(monkeys)
    for round in range(20):
        for i in range(len(monkeys)):
            items, operation = monkeys[i][0], monkeys[i][1]
            test, throw = monkeys[i][2][0], monkeys[i][3]
            for item in items:
                if operation[-1] == 'old':
                    value = item
                else:
                    value = operation[-1]
                if operation[0] == '+':
                    worry_level = item + value
                else:
                    worry_level = item * value
                worry_level = worry_level // 3
                if worry_level % test == 0:
                    monkeys[throw[0]][0].append(worry_level)
                else:
                    monkeys[throw[1]][0].append(worry_level)

            times[i] += len(monkeys[i][0])
            monkeys[i][0] = []

        print('Round:', round+1)
        for line in monkeys:
            print(line[0])

        print(times)

    times = sorted(times, reverse=True)

    return times[0] * times[1]


def part2(monkeys):
    #items_updated = [[] * len(monkeys)]
    times = [0] * len(monkeys)
    for round in range(20):
        for i in range(len(monkeys)):
            items, operation = monkeys[i][0], monkeys[i][1]
            test, throw = monkeys[i][2][0], monkeys[i][3]
            for item in items:
                if operation[-1] == 'old':
                    value = item
                else:
                    value = operation[-1]
                if operation[0] == '+':
                    worry_level = item + value
                else:
                    worry_level = item * value
                worry_level = worry_level  # not divided by 3
                if worry_level % test == 0:
                    monkeys[throw[0]][0].append(worry_level)
                else:
                    monkeys[throw[1]][0].append(worry_level)

            times[i] += len(monkeys[i][0])
            print('monkys:', i, monkeys[i][0])
            monkeys[i][0] = []

        print('Round:', round+1)
        # for line in monkeys:
        #     print(line[0])

        print(times)

    times = sorted(times, reverse=True)

    return times[0] * times[1]


def main():
    with open("test", "r") as f:
        # [items, operation, test, [true false]]
        monkeys = []
        for line in f.readlines():
            if line == '/n':
                continue
            line = line.strip()
            #print(line)
            if 'Monkey' in line:
                monkeys.append([])
            if line.startswith('Starting items'):
                items = line.split(':')[-1]
                items = items.split(',')
                items = [int(item) for item in items]
                monkeys[-1].append(items)
            if line.startswith('Operation'):
                line_list = line.split(' ')
                if line_list[-1] == 'old':
                    operation = [line_list[-2], line_list[-1]]
                else:
                    operation = [line_list[-2], int(line_list[-1])]
                monkeys[-1].append(operation)
            if line.startswith('Test'):
                line_list = line.split(' ')
                monkeys[-1].append([int(line_list[-1])])
            if line.startswith('If true'):
                line_list = line.split(' ')
                monkeys[-1].append([int(line_list[-1])])
            if line.startswith('If false'):
                line_list = line.split(' ')
                monkeys[-1][-1].append(int(line_list[-1]))
        print(monkeys)

    #print("part 1:", part1(monkeys[:]))
    print("part 2:", part2(monkeys[:]))


main()