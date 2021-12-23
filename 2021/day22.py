from collections import defaultdict


def part1(steps):
    positions = set()
    for step in steps:
        x_left, x_right = max(-50, step[1][0]), min(50, step[1][1])
        y_left, y_right = max(-50, step[2][0]), min(50, step[2][1])
        z_left, z_right = max(-50, step[3][0]), min(50, step[3][1])
        if x_left > x_left or y_left > y_right or z_left > z_right:
            continue
        for x in range(x_left, x_right + 1):
            for y in range(y_left, y_right + 1):
                for z in range(z_left, z_right + 1):
                    if step[0] == 'on':
                        if (x, y, z) not in positions:
                            positions.add((x, y, z))
                    elif step[0] == 'off':
                        if (x, y, z) in positions:
                            positions.remove((x, y, z))

    return len(positions)


def part2(steps):
    def isintersect(new_area, area):
        p_x1, p_y1, p_z1 = max(new_area[0][0], area[0][0]), max(new_area[0][1], area[0][1]), max(new_area[0][2], area[0][2])
        p_x2, p_y2, p_z2 = min(new_area[1][0], area[1][0]), min(new_area[1][1], area[1][1]), min(new_area[1][2], area[1][2])

        if p_x1 > p_x2 or p_y1 > p_y2 or p_z1 > p_z2:
            return False
        else:
            return True


    def intersection(new_area, area):
        p_x1, p_y1, p_z1 = max(new_area[0][0], area[0][0]), max(new_area[0][1], area[0][1]), max(new_area[0][2], area[0][2])
        p_x2, p_y2, p_z2 = min(new_area[1][0], area[1][0]), min(new_area[1][1], area[1][1]), min(new_area[1][2], area[1][2])

        return ((p_x1, p_y1, p_z1), (p_x2, p_y2, p_z2))


    def get_area(area):
        res = 1
        for i in range(3):
            res *= (area[1][i] - area[0][i] + 1)
        return res


    areas = defaultdict(int)
    for step in steps:
        point1 = (step[1][0], step[2][0], step[3][0])
        point2 = (step[1][1], step[2][1], step[3][1])
        new_area = (point1, point2)
        updated_areas = defaultdict(int)
        if step[0] == 'on':
            updated_areas[new_area] += 1

        for area, value in areas.items():
            if isintersect(new_area, area):
                intersection_area = intersection(new_area, area)
                updated_areas[intersection_area] -= value

        for key in updated_areas.keys():
            if key in areas.keys():
                areas[key] += updated_areas[key]
            else:
                areas[key] = updated_areas[key]

    return sum(get_area(area) * value for area, value in areas.items())


def main():
    with open('input/input22.txt', 'r') as f:
        text = f.read().splitlines()

    steps = []
    for line in text:
        step = line.strip().split(' ')
        #print(step)
        xyz = step[1].split(',')
        #print(xyz)
        element = [step[0]]
        for coordinate in xyz:
            points = coordinate[2:].split('..')
            element.append([int(points[0]), int(points[1])])
        steps.append(element)
    print(steps)
    print("part 1:", part1(steps))
    print("part 2:", part2(steps))


main()


import re
import sys
from math import prod
from collections import Counter

def intersects(a, b):
    return all(a[i] <= b[i + 1] and a[i + 1] >= b[i] for i in range(0, 5, 2))

def get_intersection_area(a, b):
    return tuple((min if i & 1 else max)(a[i], b[i]) for i in range(6))

def get_area(area):
    return prod(area[i + 1] - area[i] + 1 for i in range(0, 5, 2))

steps = [
    (line.split(' ')[0], tuple(map(int, re.findall(r'-?\d+', line))))
    for line in open(f'input/input22.txt', 'r')
]
print(steps)

areas = Counter()

for step_type, new_area in steps:
    updated_areas = Counter()

    if (step_type == 'on'):
        updated_areas[new_area] += 1

    for area, value in areas.items():
        if (intersects(new_area, area)):
            intersection_area = get_intersection_area(new_area, area)
            updated_areas[intersection_area] -= value

    areas.update(updated_areas)

print(areas)
print(sum(get_area(area) * value for area, value in areas.items()))