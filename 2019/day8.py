def part1(layers):
    min_count_0 = len(layers[0])
    layer_id = -1
    for i, layer in enumerate(layers):
        count_0 = 0
        for pixel in layer:
            if pixel == 0:
                count_0 += 1
        if count_0 < min_count_0:
            min_count_0 = count_0
            layer_id = i

    count_1 = 0
    count_2 = 0
    for pixel in layers[layer_id]:
        if pixel == 1:
            count_1 += 1
        elif pixel == 2:
            count_2 += 1

    return count_1 * count_2


def part2(layers):
    final_layer = []
    for j in range(len(layers[0])):
        for i in range(len(layers)):
            pixel = layers[i][j]
            if pixel == 2:
                continue
            else:
                final_layer.append(pixel)
                break

    final_image = []
    for i in range(0, len(final_layer), 25):
        row = [str(pixel) for pixel in final_layer[i: i + 25]]
        final_image.append(' '.join(row))

    for row in final_image:
        print(row)


def main():
    with open('input/input8.txt', 'r') as f:
        f = f.read().strip()

    f = [int(pixel) for pixel in f]
    layers = []
    for i in range(0, len(f), 25 * 6):
        layers.append(f[i: i + 25 * 6])

    ans1 = part1(layers)
    print('part1:', ans1)
    print('part2:')
    part2(layers)


main()