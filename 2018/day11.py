def generate_cells(serial_number):
    cells = {}
    for row in range(300, 0, -1):
        for col in range(300, 0, -1):
            rack_ID = col + 10
            power_level = rack_ID * row
            power_level = power_level + serial_number
            power_level = power_level * rack_ID
            hundreds_digit = (power_level // 100) % 10
            hundreds_digit = hundreds_digit - 5
            cells[(row, col)] = hundreds_digit  # cur = cur + right + down - right_down
            if row + 1 <= 300:  # except the bottom line
                cells[(row, col)] += cells[(row+1, col)]
            if col + 1 <= 300:  # except the right most line
                cells[(row, col)] += cells[(row, col+1)]
            if row + 1 <= 300 and col + 1 <= 300:
                cells[(row, col)] -= cells[(row+1, col+1)]
    return cells


def solution(cells, size):
    largest_power = 0
    pos_row, pos_col = 0, 0

    for row in range(1, 301-size+1):
        for col in range(1, 301-size+1):
            if row + size <= 300 and col + size <= 300:
                square_total_power = cells[(row, col)] - cells[(row+size, col)] \
                                     - cells[(row, col+size)] + cells[(row+size, col+size)]
            elif row + size <= 300:
                square_total_power = cells[(row, col)] - cells[(row + size, col)]
            elif col + size <= 300:
                square_total_power = cells[(row, col)] - cells[(row, col + size)]
            else:
                square_total_power = cells[(row, col)]
            if square_total_power > largest_power:
                largest_power = square_total_power
                pos_row, pos_col = row, col

    return pos_col, pos_row, largest_power


def main():
    with open('input/input11.txt') as f:
        serial_number = int(f.read().strip())  # 4455

    cells = generate_cells(serial_number)  # record the sum of position's all left and down
    col, row, _ = solution(cells, 3)
    print('part 1:', str(col) + ',' + str(row))

    col, row = 0, 0
    largest_power_size, largest_power = 0, 0
    for size in range(1, 301):
        cur_col, cur_row, cur_largest_power = solution(cells, size)
        if cur_largest_power > largest_power:
            largest_power = cur_largest_power
            col, row, largest_power_size = cur_col, cur_row, size
    print('part 2:', str(col) + ',' + str(row) + ',' + str(largest_power_size))


main()


# serial_number = 4455
#
# def generate_cells(serial_number):
#     cells = {}
#     for row in range(1, 301):
#         for col in range(1, 301):
#             rack_ID = col + 10
#             power_level = rack_ID * row
#             power_level = power_level + serial_number
#             power_level = power_level * rack_ID
#             hundreds_digit = (power_level // 100) % 10
#             hundreds_digit = hundreds_digit - 5
#             cells[(row, col)] = hundreds_digit
#     return cells
#
# direction = [(-1, -1), (-1, 0), (-1, 1),
#        (0, -1), (0, 0), (0, 1),
#        (1, -1), (1, 0), (1, 1)]
#
# largest_power = 0
# pos_row, pos_col = 0, 0
# for row in range(2, 300):
#     for col in range(2, 300):
#         square_total_power = 0
#         for (dir_row, dir_col) in direction:
#             square_total_power += grid[(row+dir_row, col+dir_col)]
#         if square_total_power > largest_power:
#             largest_power = square_total_power
#             pos_row, pos_col = row, col
# ans = str(pos_col-1) + ',' + str(pos_row-1)
# print('part 1:', ans)
