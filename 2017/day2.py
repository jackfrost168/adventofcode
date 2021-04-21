def part1(spreadsheet):
    answer = 0
    for line in spreadsheet:
        largest = max(line)
        smallest = min(line)
        answer += largest - smallest
    return answer


def part2(spreadsheet):
    answer = 0
    for line in spreadsheet:
        for num1 in line:
            for num2 in line:
                if num2 % num1 == 0 and num2 != num1:
                    answer += num2 // num1
                    break
    return answer


def main():
    with open('input/input2.txt', 'r') as f:
        f = f.readlines()
        spreadsheet = []
        for line in f:
            line = [int(num) for num in line.split()]
            spreadsheet.append(line)
    answer1 = part1(spreadsheet)
    print('part1:', answer1)
    answer2 = part2(spreadsheet)
    print('part2:', answer2)


main()
