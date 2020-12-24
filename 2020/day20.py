import copy
side_length = 12


def rotating(image, i):
    new_image = image[:]
    for _ in range(i):
        new_image[:] = map(list, zip(*new_image[::-1]))
    new_image = ["".join(line) for line in new_image]
    return new_image


def flipping(image, j):
    new_image = image[:]
    new_image = [list(line) for line in new_image]
    row = len(new_image)
    col = len(new_image[0])
    if j == 0:
        pass
    elif j == 1:  # up/down
        for i in range(row // 2):
            new_image[i], new_image[row - 1 - i] = new_image[row - 1 - i], new_image[i]
    else:  # left/right not needed
        for m in new_image:
            for j in range(col // 2):
                m[j], m[col - 1 - j] = m[col - 1 - j], m[j]
    new_image = [''.join(line) for line in new_image]
    return new_image


def put_on(big_image, image, x, y):
    big_image[(x, y)] = image


def put_off(big_image, image, x, y):
    del big_image[(x, y)]


def border_correct(big_image, x, y):
    if 0 <= x + 0 < side_length and 0 <= y + 1 < side_length and (x, y+1) in big_image.keys():
        neighbor_image = big_image[(x, y+1)]
        image = big_image[(x, y)]
        for i in range(10):
            if image[i][-1] != neighbor_image[i][0]:
                return False
    if 0 <= x + 0 < side_length and 0 <= y - 1 < side_length and (x, y-1) in big_image.keys():
        neighbor_image = big_image[(x, y - 1)]
        image = big_image[(x, y)]
        for i in range(10):
            if image[i][0] != neighbor_image[i][-1]:
                return False
    if 0 <= x + 1 < side_length and 0 <= y + 0 < side_length and (x+1, y) in big_image.keys():
        neighbor_image = big_image[(x + 1, y)]
        image = big_image[(x, y)]
        for i in range(10):
            if image[-1][i] != neighbor_image[0][i]:
                return False
    if 0 <= x - 1 < side_length and 0 <= y + 0 < side_length and (x-1, y) in big_image.keys():
        neighbor_image = big_image[(x - 1, y)]
        image = big_image[(x, y)]
        for i in range(10):
            if image[0][i] != neighbor_image[-1][i]:
                return False
    return True


def part1(images, big_image, used, x, y, stop):
    if stop[0]:
        return
    IDs = [key for key in images]
    for key in IDs:
        image = copy.deepcopy(images[key])
        if key in used:
            continue
        else:
            used.append(key)
        for i in range(4):
            rotated_image = rotating(image, i)
            for j in range(2):
                flipped_image = flipping(rotated_image, j)
                put_on(big_image, flipped_image, x, y)
                if border_correct(big_image, x, y):
                    if x == side_length-1 and y == side_length-1:
                        print('part1:', used[0]*used[side_length-1]*used[side_length*(side_length-1)]*used[-1])
                        stop[0] = True
                        global final_image
                        final_image = copy.deepcopy(big_image)
                        return
                    elif y+1 >= side_length:
                        part1(images, big_image, used, x+1, 0, stop)
                    else:
                        part1(images, big_image, used, x, y+1, stop)
                put_off(big_image, flipped_image, x, y)
        used.pop()


def remove_border(final_image):
    for key in final_image.keys():
        final_image[key].pop(0)
        final_image[key].pop()
        for i, line in enumerate(final_image[key]):
            line = list(line)
            line.pop(0)
            line.pop()
            line = ''.join(line)
            final_image[key][i] = line


def merge(final_image):
    remove_border(final_image)
    actual_image = []
    for i in range(side_length):
        for k in range(len(final_image[(0, 0)][0])):
            row = ''
            for j in range(side_length):
                row = row + final_image[(i, j)][k]
            actual_image.append(row)
    return actual_image


def monster_coordinate(monster):
    monster_position = []
    for i in range(len(monster)):
        for j in range(len(monster[i])):
            if monster[i][j] == '#':
                monster_position.append((i, j))
    return monster_position


def part2(monster_position, actual_image):
    for r in range(4):
        rotated_image = rotating(actual_image, r)
        for f in range(2):
            flipped_image = flipping(rotated_image, f)

            count_monster = 0
            sea_mask = [[0] * len(flipped_image[0]) for _ in range(len(flipped_image))]
            for i in range(len(flipped_image)):
                for j in range(len(flipped_image[i])):
                    count = 0
                    for (x, y) in monster_position:
                        if 0 <= x+i < len(flipped_image) and 0 <= y+j < len(flipped_image[i]):
                            if flipped_image[x + i][y + j] == '#':
                                count = count + 1
                            else:
                                break
                        else:
                            break
                    if count == len(monster_position):
                        count_monster += 1
                        for (x, y) in monster_position:
                            sea_mask[x+i][y+j] = 1
                    else:
                        continue

            if count_monster != 0:
                ans = 0
                for i in range(len(sea_mask)):
                    for j in range(len(sea_mask[0])):
                        if sea_mask[i][j] == 0 and flipped_image[i][j] == '#':
                            ans = ans + 1
                print('part2:', ans)
                return


final_image = {}


def main():
    with open('input/input20.txt', 'r') as f:
        f = f.readlines()
        images = {}
        for line in f:
            line = line.strip()
            if line.startswith('Tile'):
                line = line.split(' ')
                key = int(line[1][0:-1])
                images[key] = []
            elif len(line) == 0:
                pass
            else:
                images[key].append(line)

    big_image = {}
    used = []
    stop = [False]

    part1(images, big_image, used, 0, 0, stop)

    monster = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']

    actual_image = merge(final_image)
    monster_position = monster_coordinate(monster)
    part2(monster_position, actual_image)


main()
