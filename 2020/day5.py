def main():
    with open("input/input5.txt", "r") as f:  # open file
        lines = f.readlines()  # read line, lines stores the txt file
        boarding_passes = [line.strip() for line in lines]

    ans = 0
    passagers = [0]*843

    for seat in boarding_passes:
        row = seat[0:7]
        column = seat[7:]
        left = 0
        right = 127
        mid_row = 0
        for character in row:
            if character == 'F':
                right = left + (right - left + 1) // 2
            else:
                left = left + (right - left + 1) //2
            mid_row = left + (right - left) // 2
        left = 0
        right = 8
        mid_col = 0
        for character in column:
            if character == 'L':
                right = left + (right - left + 1) // 2
            else:
                left = left + (right - left + 1) // 2
            mid_col = left + (right - left) // 2
        id = 8 * mid_row + mid_col
        passagers[id] = 1
        for r in [0]:
            for c in range(0, 8):
                cur_id = r * 8 + c
                passagers[cur_id] = 1
        if id > ans:
            ans = id

    print("part1:", ans)

    myid = 0
    for i in range(len(passagers)):
        if passagers[i] == 0:
            myid = i
    print("part2:", myid)


main()
