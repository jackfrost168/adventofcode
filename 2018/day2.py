def part1(input):
    two = 0
    three = 0
    for string in input:
        appeared = {}
        have_two = False
        have_three = False
        for s in string:
            if s not in appeared.keys():
                appeared[s] = 1
            else:
                appeared[s] += 1
        for key in appeared.keys():
            if appeared[key] == 2:
                have_two = True
            if appeared[key] == 3:
                have_three = True
        if have_two == True:
            two = two + 1
        if have_three == True:
            three = three + 1
    return two*three


def part2(input):
    for i in range(len(input)):
        string1 = input[i]
        for j in range(i+1, len(input)):
            string2 = input[j]
            diff = 0
            for k in range(len(input[0])):
                if string1[k] != string2[k]:
                    diff += 1
            if diff == 1:
                ans = ''
                for m in range(len(input[0])):
                    if string1[m] == string2[m]:
                        ans = ans + string1[m]
                return ans


def main():
    with open("input/input2.txt", "r") as f: # open file
        lines = f.readlines()  # read line, lines stores the txt file
        input = [line.strip() for line in lines]

    ans1 = part1(input)
    print('part1:', ans1)
    ans2 = part2(input)
    print('part2:', ans2)


main()