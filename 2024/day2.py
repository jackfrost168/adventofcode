def check_safe(report):
    safe = True
    if report[0] > report[1]:
        for i in range(len(report) - 1):
            if report[i] - report[i + 1] > 3 or report[i] <= report[i + 1]:
                safe = False
                break
    elif report[0] < report[1]:
        for i in range(len(report) - 1):
            if report[i + 1] - report[i] > 3 or report[i + 1] <= report[i]:
                safe = False
                break
    else:
        safe = False

    return safe


def part1(reports):
    safe_count = 0
    for report in reports:
        safe = check_safe(report)

        if safe == True:
            safe_count += 1

    return safe_count


def part2(reports):
    safe_count = 0
    for report in reports:
        safe = check_safe(report)

        if safe == True:
            safe_count += 1
        elif safe == False:
            for i in range(len(report)):
                new_report = report[:]
                new_report.pop(i)
                new_safe = check_safe(new_report)
                if new_safe == True:
                    safe_count += 1
                    break

    return safe_count


def main():
    with open("input/input2.txt", "r") as f:
        reports = [[int(ele) for ele in line.strip().split()] for line in f]

    print("part 1:", part1(reports))
    print("part 2:", part2(reports))


main()
