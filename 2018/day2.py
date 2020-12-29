def part1(candidates):
    two, three = 0, 0
    for string in candidates:
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
        if have_two:
            two = two + 1
        if have_three:
            three = three + 1
    return two * three


def part2(candidates):
    for i in range(len(candidates)):
        string1 = candidates[i]
        for j in range(i+1, len(candidates)):
            string2 = candidates[j]
            diff = 0
            for k in range(len(candidates[0])):
                if string1[k] != string2[k]:
                    diff += 1
            if diff == 1:
                ans = ''
                for m in range(len(candidates[0])):
                    if string1[m] == string2[m]:
                        ans = ans + string1[m]
                return ans


def main():
    with open("input/input2.txt", "r") as f:  # open file
        candidates = [line.strip() for line in f]

    ans1 = part1(candidates)
    print('part 1:', ans1)
    ans2 = part2(candidates)
    print('part 2:', ans2)


main()
