def Intcode(input, value1, value2):
    input[1] = value1
    input[2] = value2
    ans = 0
    i = 0
    while i < len(input):
        pos1 = input[i + 1]
        pos2 = input[i + 2]
        pos_output = input[i + 3]

        if input[i] == 1:
            input[pos_output] = input[pos1] + input[pos2]
        elif input[i] == 2:
            input[pos_output] = input[pos1] * input[pos2]
        else:
            ans = input[0]
            break
        i = i + 4
    return ans


def main():

    with open('input/input2.txt') as f:
        input = [int(s) for s in f.read().strip().split(',')]
    input_copy = input[:]
    ans1 = Intcode(input_copy, 12, 2)
    print("part1:", ans1)

    ans2 = 0
    for i in range(100):
        for j in range(100):
            input_copy = input[:]
            output = Intcode(input_copy, i, j)
            if output == 19690720:
                ans2 = i * 100 + j
        if ans2 != 0:
            break
    print("part2:", ans2)


main()