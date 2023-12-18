def solution(input, part=1):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directions = ['R', 'D', 'L', 'U']
    boundary = []
    cur_x, cur_y = 0, 0
    boundary_length = 0
    for line in input:
        if part == 1:
            direction, steps = line[0], int(line[1])
            dir = dirs[directions.index(direction)]
        else:
            direction, steps= line[-1][-2], int(line[-1][2:-2], 16)
            dir = dirs[int(direction)]

        boundary_length += steps
        cur_x, cur_y = cur_x + dir[0] * steps, cur_y + dir[1] * steps
        boundary.append((cur_x, cur_y))

    area = 0
    # Shoelace formula
    for i in range(len(boundary)):
        x1, x2 = boundary[i]
        y1, y2 = boundary[(i+1)%len(boundary)]
        area += x1*y2 - x2*y1

    # Pick's theorem
    result = abs(area/2) + 1 - boundary_length/2 + boundary_length

    return int(result)


def main():
    with open('input/input18.txt') as f:
        input = [line.strip().split() for line in f.readlines()]
    #    Pick's_theorem: https://en.wikipedia.org/wiki/Pick's_theorem
    #    Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula

    print('part1:', solution(input[:], part=1))
    print('part2:', solution(input[:], part=2))

main()
