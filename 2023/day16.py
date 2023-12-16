from collections import defaultdict
import sys
sys.setrecursionlimit(5000)


def solution(map, part=1):

    def dfs(i, j, dir):
        if 0 <= i <= len(map) - 1 and 0 <= j <= len(map[0]) - 1:
            if marked[i][j] == 0:
                marked[i][j] = 1
                paths[(i, j)] = [dir]
            else:
                if dir in paths[(i, j)]:
                    return
                else:
                    paths[(i, j)].append(dir)
            if map[i][j] == '.':
                dfs(i + dir[0], j + dir[1], dir)
            elif map[i][j] == '\\':
                if dir == (0, 1):
                    dfs(i + 1, j, (1, 0))
                elif dir == (0, -1):
                    dfs(i - 1, j, (-1, 0))
                elif dir == (1, 0):
                    dfs(i, j + 1, (0, 1))
                elif dir == (-1, 0):
                    dfs(i, j - 1, (0, -1))
            elif map[i][j] == '/':
                if dir == (0, 1):
                    dfs(i - 1, j, (-1, 0))
                elif dir == (0, -1):
                    dfs(i + 1, j, (1, 0))
                elif dir == (1, 0):
                    dfs(i, j - 1, (0, -1))
                elif dir == (-1, 0):
                    dfs(i, j + 1, (0, 1))
            elif map[i][j] == '|':
                if dir == (1, 0) or dir == (-1, 0):
                    dfs(i + dir[0], j, dir)
                else:
                    dfs(i - 1, j, (-1, 0))
                    dfs(i + 1, j, (1, 0))
            elif map[i][j] == '-':
                if dir == (0, 1) or dir == (0, -1):
                    dfs(i, j + dir[1], dir)
                else:
                    dfs(i, j + 1, (0, 1))
                    dfs(i, j - 1, (0, -1))

    if part == 1:
        marked = [[0 for j in range(len(map[0]))] for i in range(len(map))]
        paths = defaultdict()
        dfs(0, 0, (0, 1))
        total = sum(sum(line) for line in marked)

        return total

    elif part == 2:

        maximum = 0
        for i in range(len(map)):
            for (j, dir) in zip([0, len(map[0])-1], [(0, 1), (0, -1)]):
                marked = [[0 for j in range(len(map[0]))] for i in range(len(map))]
                paths = defaultdict()
                dfs(i, j, dir)
                total = sum(sum(line) for line in marked)
                if total > maximum:
                    maximum = total

        for j in range(len(map[0])):
            for (i, dir) in zip([0, len(map)-1], [(1, 0), (-1, 0)]):
                marked = [[0 for j in range(len(map[0]))] for i in range(len(map))]
                paths = defaultdict()
                dfs(i, j, dir)
                total = sum(sum(line) for line in marked)
                if total > maximum:
                    maximum = total

        return maximum


def main():
    with open('input/input16.txt') as f:
        map = [list(line.strip()) for line in f.readlines()]

        print('part1:', solution(map[:], part=1))
        print('part2:', solution(map[:], part=2))

main()
