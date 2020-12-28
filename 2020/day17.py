def neighbor_list(coordinate, dimension):
    neighbors = []
    if dimension == 3:
        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]

        for x_d in [-1, 0, 1]:
            for y_d in [-1, 0, 1]:
                for z_d in [-1, 0, 1]:
                    neighbors.append((x+x_d, y+y_d, z+z_d))
        neighbors.remove((x, y, z))

    elif dimension == 4:
        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]
        w = coordinate[3]

        for x_d in [-1, 0, 1]:
            for y_d in [-1, 0, 1]:
                for z_d in [-1, 0, 1]:
                    for w_d in [-1, 0, 1]:
                        neighbors.append((x+x_d, y+y_d, z+z_d, w+w_d))
        neighbors.remove((x, y, z, w))

    return neighbors


def update_coordinates(coordinates, dimension):
    active_neighbor_count = {}
    for coordinate in coordinates.keys():
        if coordinates[coordinate] == '#':
            neighbors = neighbor_list(coordinate, dimension)
            for neighbor in neighbors:
                if neighbor in active_neighbor_count.keys():
                    active_neighbor_count[neighbor] += 1
                else:
                    active_neighbor_count[neighbor] = 1
    new_coordinates = {}
    active_count = 0

    for coordinate in active_neighbor_count.keys():
        if coordinate in coordinates.keys():
            cur_state = coordinates[coordinate]
        else:
            cur_state = '.'
        if cur_state == '#' and (not 2 <= active_neighbor_count[coordinate] <= 3):
            new_coordinates[coordinate] = '.'
        elif cur_state == '.' and active_neighbor_count[coordinate] == 3:
            new_coordinates[coordinate] = '#'
        else:
            new_coordinates[coordinate] = cur_state

        if new_coordinates[coordinate] == '#':
            active_count += 1
    return new_coordinates, active_count


def main():
    with open('input/input17.txt', 'r') as f:
        init = [line.strip() for line in f]
    coordinates_3d = {}
    for i in range(len(init)):
        for j in range(len(init[0])):
            coordinates_3d[(i, j, 0)] = init[i][j]

    coordinates_4d = {}
    for i in range(len(init)):
        for j in range(len(init[0])):
            coordinates_4d[(i, j, 0, 0)] = init[i][j]

    count_3d, count_4d = 0, 0
    for _ in range(6):
        coordinates_3d, count_3d = update_coordinates(coordinates_3d, 3)
        coordinates_4d, count_4d = update_coordinates(coordinates_4d, 4)
    print('part 1:', count_3d)
    print('part 2:', count_4d)


main()


# with open('input/input17.txt', 'r') as f:
#     init = [line.strip() for line in f]
#
# def augment(input):
#     new_state = []
#     new_layer = ['.'*(len(input[0][0])+2)]*(len(input[0])+2)
#     new_state.append(new_layer)
#
#     for layer in input:
#         new_layer = []
#         new_layer.append('.'*(len(layer[0])+2))
#         for line in layer:
#             new_line = '.' + line + '.'
#             new_layer.append(new_line)
#         new_layer.append('.'*(len(layer[0])+2))
#         new_state.append(new_layer)
#     new_layer = ['.'*(len(input[0][0])+2)]*(len(input[0])+2)
#     new_state.append(new_layer)
#     return new_state
#
# input = [init]
#
#
# import copy
# direction = [(x, y, z) for x in [-1,0,1] for y in [-1,0,1] for z in [-1,0,1]]
# direction.remove((0,0,0))
# print(len(direction))
# cycle = 0
# while cycle < 6:
#     new_state = augment(input)
#     input = copy.deepcopy(new_state)
#     for i in range(0, len(new_state)):
#         for j in range(0, len(new_state[0])):
#             for k in range(0, len(new_state[0][0])):
#                 count_active = 0
#                 count_inactive = 0
#                 for (x, y, z) in direction:
#                     if 0 <= i + x < len(new_state) and \
#                         0 <= j + y < len(new_state[0]) and \
#                         0 <= k + z < len(new_state[0][0]):
#                         if new_state[i+x][j+y][k+z] == '.':
#                             count_inactive += 1
#                         else:
#                             count_active += 1
#                 if new_state[i][j][k] == '.':
#                     if count_active == 3:
#                         string_list = list(input[i][j])
#                         string_list[k] = '#'
#                         string = ''.join(string_list)
#                         input[i][j] = string
#                 elif new_state[i][j][k] == '#':
#                     if count_active == 2 or count_active == 3:
#                         continue
#                     else:
#                         string_list = list(input[i][j])
#                         string_list[k] = '.'
#                         string = ''.join(string_list)
#                         input[i][j] = string
#
#     cycle = cycle + 1
#
# ans = 0
# for layer in input:
#     for line in layer:
#         for s in line:
#             if s == '#':
#                 ans = ans + 1
# print('part1:', ans)
