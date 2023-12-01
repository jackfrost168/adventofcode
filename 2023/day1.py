def part1(digits):
    total = 0
    for line in digits:
        for i in line:
            if i in '0123456789':
                first_digit = i
                break
        for i in line[::-1]:
            if i in '0123456789':
                second_digit = i
                break

        digit = int(first_digit + second_digit)
        total += digit

    return total

def part2(digits):
    total = 0
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for line in digits:
        for i in range(len(line)):
            if line[i] in '0123456789':
                first_digit_num, pos_num = int(line[i]), i
                break
        first_digit_text = ''
        pos_text = 100000
        for i in range(len(line)-3):
            if line[i: i+3] in numbers.keys():
                first_digit_text, pos_text = numbers[line[i: i+3]], i
                break
            elif i <= len(line) - 4 and line[i: i + 4] in numbers.keys():
                first_digit_text, pos_text = numbers[line[i: i+4]], i
                break
            elif i <= len(line) - 5 and line[i: i + 5] in numbers.keys():
                first_digit_text, pos_text = numbers[line[i: i + 5]], i
                break

        first_digit = first_digit_num if pos_num <= pos_text else int(first_digit_text)

        for i in range(len(line)-1, -1, -1):
            if line[i] in '0123456789':
                second_digit_num, pos = int(line[i]), i
                break
        second_digit_text = ''
        pos_text = -1
        for i in range(len(line)-3, -1, -1):
            if line[i: i+3] in numbers.keys():
                second_digit_text, pos_text = numbers[line[i: i+3]], i
                break
            elif i <= len(line) - 4 and line[i: i + 4] in numbers.keys():
                second_digit_text, pos_text = numbers[line[i: i+4]], i
                break
            elif i <= len(line) - 5 and line[i: i + 5] in numbers.keys():
                second_digit_text, pos_text = numbers[line[i: i + 5]], i
                break

        second_digit = second_digit_num if pos >= pos_text else int(second_digit_text)

        num = first_digit * 10 + second_digit
        total += num

    return total


def main():
    with open("input/input1.txt", "r") as f:
        digits = [line.strip() for line in f.readlines()]

    print("part 1:", part1(digits))
    print("part 2:", part2(digits))


main()
