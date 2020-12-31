def part1(coordinates, closest_locations, max_height, max_width):
    for i in range(max_height+1):
        for j in range(max_width+1):
            distances = []
            for (x, y) in coordinates:
                distances.append(abs(i-x)+abs(y-j))
            closest_distance = min(distances)
            if distances.count(closest_distance) == 1:
                coordinate = coordinates[distances.index(closest_distance)]
                closest_locations[coordinate] += 1

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
            if closest_locations[(x, y)] > largest_area:
                largest_area = closest_locations[(x, y)]

    return largest_area


def part2(coordinates, max_height, max_width):
    valid_regions = 0
    for i in range(max_height+1):
        for j in range(max_width+1):
            total_distance = 0
            for (x, y) in coordinates:
                total_distance += abs(x-i) + abs(y-j)
            if total_distance < 10000:
                valid_regions += 1

    return valid_regions


def main():
    with open('input/input6.txt', 'r') as f:
        coordinates = []  # [(0, 0), (1, 2)]
        closest_locations = {}  # {(0, 2): 0, (1, 2): 0}
        for line in f:
            line = line.strip().split(', ')
            x, y = int(line[0]), int(line[1])
            coordinates.append((x, y))
            closest_locations[(x, y)] = 0

    max_height = max([coordinate[0] for coordinate in coordinates])
    max_width = max([coordinate[1] for coordinate in coordinates])

    largest_area = part1(coordinates, closest_locations, max_height, max_width)
    print('part 1:', largest_area)
    valid_regions = part2(coordinates, max_height, max_width)
    print('part 2:', valid_regions)


main()
