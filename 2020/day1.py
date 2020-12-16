def sum2(arr):
    for a in arr:
        if 2020 - a in arr:
            ans = a * (2020 - a)
            return ans


def sum3(arr):
    arr = sorted(arr)
    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] > 2020:
                k = k - 1
            elif arr[i] + arr[j] + arr[k] < 2020:
                j = j + 1
            else:
                ans = arr[i] * arr[j] * arr[k]
                return ans


def main():
    f = open("input/input1.txt", "r")  # open file
    lines = f.readlines()  # read line, lines stores the txt file
    input = [int(line.strip()) for line in lines]
    # for line in lines:
    #     line = line.strip('\n')  # take away '\n'
    #     input.append(int(line))

    ans1 = sum2(input)
    print("part1:", ans1)
    ans2 = sum3(input)
    print("part2:", ans2)


main()