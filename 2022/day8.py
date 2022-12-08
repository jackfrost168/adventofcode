import numpy as np


def part1(trees):
    count = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            tree = trees[i][j]
            left2right = trees[i, 0: j].tolist()
            right2left = trees[i, j+1:].tolist()
            top2bottom = trees[0: i, j].tolist()
            bottom2top = trees[i+1:, j].tolist()
            left_vis, right_vis, top_vis, bottom_vis = True, True, True, True
            for t in left2right:
                if tree <= t:
                    left_vis = False
                    break
            for t in right2left:
                if tree <= t:
                    right_vis = False
                    break
            for t in top2bottom:
                if tree <= t:
                    top_vis = False
                    break
            for t in bottom2top:
                if tree <= t:
                    bottom_vis = False
                    break
            if left_vis or right_vis or top_vis or bottom_vis:
                count += 1

    return count + 2 * len(trees) + 2 * len(trees[0]) - 4


def part2(trees):
    scenic_score = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            tree = trees[i][j]
            left2right = trees[i, 0: j].tolist()
            right2left = trees[i, j + 1:].tolist()
            top2bottom = trees[0: i, j].tolist()
            bottom2top = trees[i + 1:, j].tolist()

            left_score, right_score, top_score, bottom_score = 0, 0, 0, 0
            for t in reversed(left2right):
                left_score += 1
                if tree <= t:
                        break
            for t in right2left:
                right_score += 1
                if tree <= t:
                    break
            for t in reversed(top2bottom):
                top_score += 1
                if tree <= t:
                    break
            for t in bottom2top:
                bottom_score += 1
                if tree <= t:
                    break

            if left_score * right_score * top_score * bottom_score > scenic_score:
                scenic_score = left_score * right_score * top_score * bottom_score

    return scenic_score


def main():
    with open("input/input8.txt", "r") as f:  # open file
        trees = [line.strip() for line in f.readlines()]
        trees = [[int(trees[i][j]) for j in range(len(trees[0]))] for i in range(len(trees))]
        trees = np.array(trees)

    print("part 1:", part1(trees))
    print("part 2:", part2(trees))


main()
