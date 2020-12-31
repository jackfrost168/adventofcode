import time
start = time.time()

with open('input/input6.txt', 'r') as f:
    coordinates = []  # [(0, 0), (1, 2)]
    closest_locations = {}  # {(0, 2): [(0, 1), (0, 2), (0, 3)]}
    for line in f:
        line = line.strip().split(', ')
        x, y = int(line[0]), int(line[1])
        coordinates.append((x, y))
        closest_locations[(x, y)] = []

print(coordinates)
print(closest_locations)
max_height = 0
max_width = 0
for (x, y) in coordinates:
    if max_width < y:
        max_width = y
    if max_height < x:
        max_height = x
print(max_height, max_width)

for i in range(max_height+1):
    for j in range(max_width+1):
        distances = []
        for (x, y) in coordinates:
            distances.append(abs(i-x)+abs(y-j))
        closest_distance = min(distances)
        if distances.count(closest_distance) == 1:
            coordinate = coordinates[distances.index(closest_distance)]
            closest_locations[coordinate].append((i, j))

largest_area = 0
for (x, y) in coordinates:
    is_infinite = []
    for (edge_x, edge_y) in [(x, 0), (x, max_width), (0, y), (max_height, y)]:
        for (other_x, other_y) in coordinates:
            if (x, y) == (other_x, other_y):
                continue
            if abs(edge_x-x) + abs(edge_y-y) > abs(edge_x-other_x) + abs(edge_y-other_y):
                is_infinite.append(False)
                break

    if len(is_infinite) < 4:
        continue
    else:
        if len(closest_locations[(x, y)]) > largest_area:
            largest_area = len(closest_locations[(x, y)])

print('part 1:', largest_area)


valid_region = 0
for i in range(max_height+1):
    for j in range(max_width+1):
        total_distance = 0
        for (x, y) in coordinates:
            total_distance += abs(x-i) + abs(y-j)
        if total_distance < 10000:
            valid_region += 1
print('part 2:', valid_region)

end = time.time()
print(end-start)
