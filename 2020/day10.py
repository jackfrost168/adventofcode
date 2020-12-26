def part1(jolts):
    value = 0
    diff1 = 0
    diff3 = 0
    while value != max(jolts):
        if value+1 in jolts:
            value = value + 1
            diff1 += 1
        elif value+2 in jolts:
            value += 2
        elif value+3 in jolts:
            value = value + 3
            diff3 += 1

    return diff3*diff1


def part2(jolts):
    array = sorted(jolts)
    base_array = []
    i = 0
    while array[i] != max(array):
        base_array.append(array[i])
        if array[i] + 3 in array:
            i = array.index(array[i]+3)
        elif array[i] + 2 in array:
            i = array.index(array[i]+2)
        elif array[i] + 1 in array:
            i = array.index(array[i]+1)
    base_array.append(max(array))

    ans = 1
    for a in base_array:
        if a+4 in base_array:
            index0, index1 = array.index(a), array.index(a+4)
            length = index1 - index0 - 1
            if length >= 1:
                ans = ans * (pow(2, length)-1)
        elif a+3 in base_array:
            index0, index1 = array.index(a), array.index(a + 3)
            length = index1 - index0 - 1
            if length >= 1:
                ans = ans * pow(2, length)
        elif a+2 in base_array:
            index0, index1 = array.index(a), array.index(a+2)
            length = index1 - index0 - 1
            if length == 1:
                ans = ans * 2
    return ans


def main():
    with open("input/input10.txt", "r") as f:
        jolts = [int(line.strip()) for line in f]
        jolts.append(0)
        jolts.append(max(jolts) + 3)

    ans1 = part1(jolts)
    print('part1:', ans1)
    ans2 = part2(jolts)
    print('part2:', ans2)


main()
