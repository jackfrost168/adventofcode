from itertools import count


def part1(almanac):
    seeds = almanac['seeds']
    keys = list(almanac.keys())[1:]
    locations = []
    for seed in seeds:
        for key in keys:
            for line in almanac[key]:
                destination, source, length = line[0], line[1], line[2]
                if source <= seed < source + length:
                    seed = seed + (destination - source)
                    break

        locations.append(seed)

    return min(locations)


def part2(almanac):
    seeds = almanac['seeds']
    keys = list(almanac.keys())[1:][::-1]

    for n in count():
        # if n % 1000000 == 0:
        #     print('n:', n)
        # Inverse process
        candidate = n
        for key in keys:
            for line in almanac[key]:
                destination, source, length = line[0], line[1], line[2]
                if destination <= n < destination + length:
                    n = n + (source - destination)
                    break

        for (seed_start, length) in zip(seeds[::2], seeds[1::2]):
            if seed_start <= n < seed_start + length:

                return candidate


def main():
    with open("input/input5.txt", "r") as f:
        input = f.read().split('\n\n')

        almanac = {}
        for (i, part) in enumerate(input):
            if i == 0:
                part = part.split(': ')
                seeds = [int(seed) for seed in part[1].split()]
                almanac['seeds'] = seeds
            else:
                part = part.split('\n')
                maps = []
                for j in range(1, len(part)):
                    map = [int(num) for num in part[j].split(' ')]
                    maps.append(map)
                almanac[part[0].split(' ')[0]] = maps

        print("part 1:", part1(almanac))
        print("part 2:", part2(almanac)) # About 20 minutes. Answer: 34039469

main()
