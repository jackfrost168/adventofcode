def part1(games):
    condition = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    game_id = 1
    for game in games:
        possible = True
        for set in game:
            for num_color in set:
                num_color = num_color.split(' ')
                num, color = int(num_color[0]), num_color[1]

                if num > condition[color]:
                    possible = False
                    break

            if possible == False:
                break

        if possible == True:
            total += game_id

        game_id += 1

    return total


def part2(games):
    summation = 0
    for game in games:
        minimum = {"red": 0, "green": 0, "blue": 0}
        for set in game:
            for num_color in set:
                num_color = num_color.split(' ')
                num = int(num_color[0])
                color = num_color[1]
                if num > minimum[color]:
                    minimum[color] = num
        power = 1
        for value in minimum.values():
            power = power * value

        summation += power

    return summation


def main():
    with open("input/input2.txt", "r") as f:
        games = []
        for line in f.readlines():
            line = line.strip().split(': ')
            cubes = line[1].split('; ')
            game_i = []
            for cube in cubes:
                cube = cube.split(', ')
                game_i.append(cube)
            games.append(game_i)

    print("part 1:", part1(games[:]))
    print("part 2:", part2(games[:]))


main()
