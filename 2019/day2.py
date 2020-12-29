def Intcode(integers, value1, value2):
    integers[1] = value1
    integers[2] = value2
    ans = 0
    i = 0
    while i < len(integers):
        pos1 = integers[i + 1]
        pos2 = integers[i + 2]
        pos_output = integers[i + 3]

        if integers[i] == 1:
            integers[pos_output] = integers[pos1] + integers[pos2]
        elif integers[i] == 2:
            integers[pos_output] = integers[pos1] * integers[pos2]
        else:
            ans = integers[0]
            break
        i = i + 4
    return ans


def main():
    with open('input/input2.txt') as f:
        integers = [int(s) for s in f.read().strip().split(',')]
    ans1 = Intcode(integers[:], 12, 2)
    print("part1:", ans1)

    ans2 = 0
    for i in range(100):
        for j in range(100):
            output = Intcode(integers[:], i, j)
            if output == 19690720:
                ans2 = i * 100 + j
        if ans2 != 0:
            break
    print("part2:", ans2)


main()
