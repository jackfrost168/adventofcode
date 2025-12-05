def part1(ranges):
    answer = 0
    for r in ranges:
        start, end = r.split('-')
        if len(start) % 2 == 1 and len(end) % 2 == 1:
            continue
        end_first_half = end[0:len(end)//2]

        if len(start) % 2 == 1 and len(end) % 2 == 0:
            min_num = str(pow(10, len(end_first_half)-1))
            max_num = end[0:len(end) // 2]
        elif len(start) % 2 == 0 and len(end) % 2 == 1:
            min_num = start[0:len(start)//2]
            max_num = end[0:len(end) // 2 + 1]
        elif len(start) % 2 == 0 and len(end) % 2 == 0:
            min_num = start[0:len(start)//2]
            max_num = end[0:len(end) // 2]

        for num in range(int(min_num), int(max_num)+1):
            #print(num)
            if int(start) <= num * pow(10, len(min_num)) + num <= int(end) and len(str(num * pow(10, len(min_num)) + num)) % 2 == 0:
                answer += num * pow(10, len(min_num)) + num

    return answer


def check_valid(number):
    str_number = str(number)
    n_digits = len(str_number)
    if n_digits <= 1:
        return False
    for i in range(1, n_digits//2+1):
        if n_digits % i == 0:
            invalid = True
            pattern = ""
            for p in range(i):
                pattern += str_number[p]
            for j in range(0, n_digits, i):
                if str_number[j:j+i] != pattern:
                    invalid = False
                    break
            if invalid == True:
                return invalid

    return invalid


def part2(ranges):
    answer = 0
    for r in ranges:
        start, end = r.split('-')
        start, end = int(start), int(end)
        for num in range(start, end+1):
            invalid = check_valid(num)
            if invalid == True:
                #print(num)
                answer += num

    return answer


def main():
    with open("input/input2.txt", "r") as f:
        inputs = f.read().strip().split(',')
    print("part 1:", part1(inputs[:]))
    print("part 2:", part2(inputs[:]))

main()
