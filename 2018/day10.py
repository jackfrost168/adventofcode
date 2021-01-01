def solution(positions, velocities):
    seconds = 0
    while True:
        new_positions = []
        for (pos_row, pos_col), (v_row, v_col) in zip(positions, velocities):
            new_row = pos_row + v_row
            new_col = pos_col + v_col
            new_positions.append((new_row, new_col))

        seconds += 1
        min_row = min([row for (row, col) in new_positions])
        max_row = max([row for (row, col) in new_positions])
        if max_row - min_row <= 10:
            min_col = min([col for (row, col) in new_positions])
            max_col = max([col for (row, col) in new_positions])
            message = []
            for i in range(min_row, max_row+1):
                row_message = ''
                for j in range(min_col, max_col+1):
                    if (i, j) in new_positions:
                        row_message += '#'
                    else:
                        row_message += ' '
                message.append(row_message)

            return message, seconds

        positions = new_positions[:]


def main():
    with open('input/input10.txt', 'r') as f:
        positions = []
        velocities = []
        for line in f:
            line = line.strip().replace('position=<', '').replace('> velocity=<', ',').replace('>', '')
            line = line.split(',')
            positions.append((int(line[1]), int(line[0])))  # [(Y, X)]
            velocities.append((int(line[3]), int(line[2])))  # [(Y, X)]

    message, seconds = solution(positions, velocities)
    print('part 1:')
    for row in message:
        print(row)
    print('part 2:', seconds)


main()
