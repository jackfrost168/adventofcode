def areas(claims):
    fabric = {}
    for key in claims.keys():
        claim = claims[key]
        x, y = claim[0], claim[1]
        width, height = claim[2], claim[3]
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


def part2(claims, fabric):
    for key in claims.keys():
        claim = claims[key]
        x, y = claim[0], claim[1]
        width, height = claim[2], claim[3]
        overlab = False
        for i in range(height):
            for j in range(width):
                if fabric[(x + i, y + j)] >= 2:
                    overlab = True
                    break
            if overlab:
                break
        if overlab is False:
            return key


def main():
    with open('input/input3.txt', 'r') as f:
        claims = {}  # {id: (576, 16, 17, 14)}
        for line in f:
            line = line.strip().replace('#', '').replace('@ ', '').replace(':', '')\
                .replace(',', ' ').replace('x', ' ').split(' ')
            ID = int(line[0])
            x, y = int(line[2]), int(line[1])
            width, height = int(line[3]), int(line[4])
            claims[ID] = (x, y, width, height)

    fabric = areas(claims)
    ans1 = part1(fabric)
    print('part 1:', ans1)
    ans2 = part2(claims, fabric)
    print('part 2:', ans2)


main()
