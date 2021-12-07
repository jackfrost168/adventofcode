def compute_cost(positiones, pos):
    cost = 0
    for i in positiones:
        cost += abs(i - pos)
    return cost


def compute_cost2(positiones, pos):
    cost = 0
    for i in positiones:
        cost += sum([num for num in range(1, abs(i-pos) + 1)])

    return cost


def part1(positiones):
    min_cost = sum(positiones)
    for i in range(len(positiones)):
        cost = compute_cost(positiones, i)
        if cost < min_cost:
            min_cost = cost

    return min_cost


def part2(positiones):
    min_cost = max(positiones) * max(positiones) * len(positiones)
    for i in range(len(positiones)):
        cost = compute_cost2(positiones, i)
        if cost < min_cost:
            min_cost = cost

    return min_cost


def main():
    with open("input/input7.txt", "r") as f:  # open file
        f = f.read().split(',')  # read line, lines stores the txt file
    positiones = [int(i) for i in f]

    ans1 = part1(positiones[:])
    print("part 1:", ans1)
    ans2 = part2(positiones[:])
    print("part 2:", ans2)


main()
