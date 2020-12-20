with open('test.txt', 'r') as f:
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

side_length = 3

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
    else:
        for m in new_image:
            for j in range(col // 2):
                m[j], m[col - 1 - j] = m[col - 1 - j], m[j]
    new_image = [''.join(line) for line in new_image]
    return new_image

# print('//////////////')
# new_image = flipping(images[2129], 1)
# for line in new_image:
#     print(line)


big_image = {}
def put_on(image, x, y):
    big_image[(x, y)] = image
    return big_image


def put_off(image, x, y):
    #big_image = big_image.pop((x, y))
    del big_image[(x, y)]
    return big_image

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

import copy
def part1(IDS, used, x, y):
    #for key in images.keys():
    if len(IDS) > 0:
        key = IDS[0]
        IDS.remove(key)
    for key in IDS:
    #for key in IDS:
        image = copy.deepcopy(images[key])
        if key in used:
            continue
        else:
            used.append(key)
            #IDS.remove(key)
        for i in range(4):
            rotated_image = rotating(image, i)
            for j in range(3):
                flipped_image = flipping(rotated_image, j)
                big_image = put_on(flipped_image, x, y)
                if border_correct(big_image, x, y):
                    if x == side_length-1 and y == side_length-1:
                        print('ans')
                        return
                    elif y+1 >= side_length:
                        y = 0
                        part1(IDS, used, x+1, y)
                    else:
                        part1(IDS, used, x, y+1)
                else:
                    big_image = put_off(flipped_image, x, y)
        used.pop()
        IDS.append(key)
used = []
IDS = [key for key in images]
part1(IDS, used, 0, 0)
