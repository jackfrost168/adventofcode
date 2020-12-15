def part1(input):
    value = 0
    diff1 = 0
    diff3 = 0
    while value != max(input):
        if value+1 in input:
            value = value + 1
            diff1 += 1
        elif value+2 in input:
            value += 2
        elif value+3 in input:
            value = value + 3
            diff3 += 1

    return diff3*diff1


def part2(input):
    array = sorted(input)
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

    tmp = 1
    for a in base_array:
        if a+4 in base_array:
            index0 = array.index(a)
            index1 = array.index(a+4)
            length = index1 - index0 - 1
            if length >= 1:
                tmp = tmp * (pow(2, length)-1)
        elif a+3 in base_array:
            index0 = array.index(a)
            index1 = array.index(a + 3)
            length = index1 - index0 - 1
            if length >= 1:
                tmp = tmp * pow(2, length)
        elif a+2 in base_array:
            index0 = array.index(a)
            index1 = array.index(a+2)
            length = index1 - index0 - 1
            if length == 1:
                tmp = tmp * 2
    return tmp


def main():
    f = open("input10.txt", "r")  # open file
    lines = f.readlines()  # read line, lines stores the txt file
    input = [int(line.strip()) for line in lines]
    input.append(0)
    input.append(max(input) + 3)

    ans1 = part1(input)
    print('part1:', ans1)
    ans2 = part2(input)
    print('part2:', ans2)


main()