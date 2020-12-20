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
#print(images)

# print(len(images.keys()))
# for line in images[2129]:
#     print(line)

side_length = 12

def rotating(image, i):
    new_image = image[:]
    for _ in range(i):
        new_image[:] = map(list,zip(*new_image[::-1]))
    new_image = ["".join(line) for line in new_image]
    return new_image


def flipping(image, j):
    new_image = image[:]
    new_image = [list(line) for line in new_image]
    row = len(new_image)
    col = len(new_image[0])
    if j == 0:
        pass
    elif j == 1: #up/down
        for i in range(row // 2):
            new_image[i], new_image[row - 1 - i] = new_image[row - 1 - i], new_image[i]
    else:  #left/right not needed
        for m in new_image:
            for j in range(col // 2):
                m[j], m[col - 1 - j] = m[col - 1 - j], m[j]
    new_image = [''.join(line) for line in new_image]
    return new_image

# print('//////////////')
# new_image = flipping(images[2129], 1)
# for line in new_image:
#     print(line)



def put_on(big_image, image, x, y):
    big_image[(x, y)] = image


def put_off(big_image, image, x, y):
    del big_image[(x, y)]



def border_correct(big_image, x, y):
    #direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #for (i, j) in direction:
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
#global stop

import copy
def part1(big_image, IDS, used, x, y, stop):
    if stop[0]:
        return
    for key in IDS:
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
                        print('ans:', used)
                        print('ans:', used[0],used[side_length-1],used[side_length*(side_length-1)],used[-1])
                        print('part1:', used[0]*used[side_length-1]*used[side_length*(side_length-1)]*used[-1])
                        stop[0] = True
                        return
                    elif y+1 >= side_length:
                        part1(big_image, IDS, used, x+1, 0, stop)
                    else:
                        part1(big_image, IDS, used, x, y+1, stop)

                put_off(big_image, flipped_image, x, y)
        used.pop()

big_image = {}
used = []
IDS = [key for key in images]
stop = [False]
part1(big_image, IDS, used, 0, 0, stop)


