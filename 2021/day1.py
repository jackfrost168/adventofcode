def part1(arr):
    # count = 0
    # for i in range(1, len(arr)):
    #     if arr[i] > arr[i-1]:
    #         count += 1

    count = sum(b > a for a, b in zip(arr, arr[1:]))

    return count


def part2(arr):
    # count = 0
    # for i in range(1, len(arr)-2):
    #     if arr[i] + arr[i+1] + arr[i+2] > arr[i-1] + arr[i] + arr[i+1]:
    #         count += 1

    count = sum(b > a for a, b in zip(arr, arr[3:]))

    return count


def main():
    with open("input/input1.txt", "r") as f:  # open file
        report = [int(line.strip()) for line in f.read().splitlines()]

    print("part 1:", part1(report))
    print("part 2:", part2(report))


main()
