def areas(input):
    fabric = {}
    for key in input.keys():
        claim = input[key]
        x = claim[0]
        y = claim[1]
        width = claim[2]
        height = claim[3]
        for i in range(height):
            for j in range(width):
                if (x+i, y+j) not in fabric.keys():
                    fabric[(x+i, y+j)] = 1
                else:
                    fabric[(x+i, y+j)] += 1
    return fabric


def part1(fabric):
    ans = 0
    for key in fabric.keys():
        if fabric[key] >= 2:
            ans = ans + 1
    return ans


def part2(input, fabric):
    for key in input.keys():
        claim = input[key]
        x = claim[0]
        y = claim[1]
        width = claim[2]
        height = claim[3]
        overlab = False
        for i in range(height):
            for j in range(width):
                if fabric[(x + i, y + j)] >= 2:
                    overlab = True
                    break
            if overlab == True:
                break
        if overlab == False:
            return key


def main():
    f = open('input/input3.txt', 'r')
    lines = f.readlines()
    input = {}
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        id = int(line[0][1:])
        pos = str(line[2]).replace(':', '')
        pos = pos.split(',')
        x = int(pos[1])
        y = int(pos[0])
        area = str(line[3]).split('x')
        width = int(area[0])
        height = int(area[1])
        input[id] = (x, y, width, height)

    fabric = areas(input)
    ans1 = part1(fabric)
    print('part1:', ans1)
    ans2 = part2(input, fabric)
    print('part2:', ans2)


main()