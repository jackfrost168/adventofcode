def part1(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            count += 1

    return count


def part2(arr):
    count = 0
    for i in range(1, len(arr)-2):
        if arr[i] + arr[i+1] + arr[i+2] > arr[i-1] + arr[i] + arr[i+1]:
            count += 1
    return count


def main():
    with open("input/input1.txt", "r") as f:  # open file
        f = f.readlines()  # read line, lines stores the txt file
        report = [int(line.strip()) for line in f]

    ans1 = part1(report)
    print("part 1:", ans1)
    ans2 = part2(report)
    print("part 2:", ans2)


main()
