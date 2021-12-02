def part1(triangles):
    num_valid = 0
    for x, y, z in triangles:
        triangle = sorted([int(x), int(y), int(z)])
        if triangle[0] + triangle[1] > triangle[2]:
            num_valid += 1

    return num_valid


def part2(traingles):
    num_valid = 0

    for i in range(0, len(traingles), 3):
        for j in range(3):
            x, y, z = sorted([int(traingles[i][j]), int(traingles[i+1][j]), int(traingles[i+2][j])])
            if x + y > z:
                num_valid += 1

    return num_valid


def main():
    with open("input/input3.txt", "r") as f:  # open file
        triangles = f.readlines()  # read line, lines stores the txt file

    triangles = [triangle.split() for triangle in triangles]

    ans1 = part1(triangles[:])
    print("part 1:", ans1)
    ans2 = part2(triangles[:])
    print("part 2:", ans2)


main()
