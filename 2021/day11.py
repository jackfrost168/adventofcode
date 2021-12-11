def dfs_neighbor(octopus, i, j, flashed):
    directions = [(-1, -1), (-1, 0), (-1, 1), \
                   (0, -1), (0, 1), \
                    (1, -1), (1, 0), (1, 1)]
    for d_x, d_y in directions:
        if 0 <= i+d_x <= len(octopus)-1 and 0 <= j+d_y <= len(octopus[0])-1:
            if octopus[i+d_x][j+d_y] <= 9:
                octopus[i+d_x][j+d_y] += 1
                if octopus[i+d_x][j+d_y] == 10 and flashed[i+d_x][j+d_y] == 0:
                    flashed[i+d_x][j+d_y] = 1
                    dfs_neighbor(octopus, i+d_x, j+d_y, flashed)


def part1(octopus):
    total_flashes = 0
    for steps in range(100):
        octopus = [[i+1 for i in line] for line in octopus]
        flashed = [[0] * len(octopus[0]) for i in range(len(octopus))]

        for i, line in enumerate(octopus):
            for j, energy in enumerate(line):
                if energy == 10 and flashed[i][j] == 0:
                    flashed[i][j] = 1
                    dfs_neighbor(octopus, i, j, flashed)

        octopus = [[num if num <= 9 else 0 for num in line] for line in octopus]

        total_flashes += sum(map(sum, flashed))

    return total_flashes


def part2(octopus):
    for steps in range(10000):
        octopus = [[i+1 for i in line] for line in octopus]
        flashed = [[0] * len(octopus[0]) for i in range(len(octopus))]

        for i, line in enumerate(octopus):
            for j, energy in enumerate(line):
                if energy == 10 and flashed[i][j] == 0:
                    flashed[i][j] = 1
                    dfs_neighbor(octopus, i, j, flashed)

        octopus = [[num if num <= 9 else 0 for num in line] for line in octopus]

        if sum(map(sum, flashed)) == len(octopus) * len(octopus[0]):
            return steps + 1


def main():
    with open("input/input11.txt", "r") as f:  # open file
        octopus = [[int(i) for i in line.strip()] for line in f.read().splitlines()]

    print("part 1:", part1(octopus[:]))
    print("part 2:", part2(octopus[:]))


main()
