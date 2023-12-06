import math

def part1(input):
    times, distances = input[0], input[1]
    num_beats = []
    for (i, time) in enumerate(times):
        beat = 0
        for t in range(time):
            record_dis = t * (time - t)
            if record_dis > distances[i]:
                beat += 1
        num_beats.append(beat)

    total = 1
    for n_beat in num_beats:
        total *= n_beat

    return total


def part2(input):
    time = int(''.join([str(t) for t in input[0]]))
    distance = int(''.join([str(d) for d in input[1]]))

    a, b, c = 1, -1*time, distance
    x1 = (-b - math.sqrt(-4 * a * c + b ** 2)) / (2 * a)
    x2 = (-b + math.sqrt(-4 * a * c + b ** 2)) / (2 * a)

    return abs(int(x1-x2)) + 1


# def part2(input):
#     time, distance = '', ''
#     for (t, d) in zip(input[0], input[1]):
#         time = time + str(t)
#         distance = distance + str(d)
#     time, distance = int(time), int(distance)
#
#     beat = 0
#     for t in range(time):
#         record_dis = t * (time - t)
#         if record_dis > distance:
#             beat += 1
#
#     return beat


def main():
    with open("input/input6.txt", "r") as f:
        input = [line.strip() for line in f.readlines()]
        input[0] = [int(t) for t in input[0].split(': ')[1].split()]
        input[1] = [int(t) for t in input[1].split(': ')[1].split()]

        print('part1:', part1(input))
        print('part2:', part2(input))


main()
