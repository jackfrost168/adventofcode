def n_neighbors(paper, i, j):
    n_rows, n_cols = len(paper), len(paper[0])
    dirs = [(-1,-1), (-1,0), (-1,1),
            (0,-1), (0,1),
            (1,-1), (1,0), (1,1)]

    n_rolls = 0
    for (dir_i, dir_j) in dirs:
        new_i, new_j = i + dir_i, j + dir_j
        if 0 <= new_i <= n_rows - 1 and 0 <= new_j <= n_cols - 1:
            if paper[new_i][new_j] == "@":
                n_rolls += 1

    return n_rolls


def part1(paper):
    answer = 0
    n_rows, n_cols = len(paper), len(paper[0])

    for i in range(n_rows):
        for j in range(n_cols):
            if paper[i][j] == "@":
                n_rolls = n_neighbors(paper, i, j)
                if n_rolls < 4:
                    answer += 1

    return answer

def part2(paper):

    paper = [list(line) for line in paper]
    answer = 0
    n_rows, n_cols = len(paper), len(paper[0])

    while True:
        remove_candidates = []
        for i in range(n_rows):
            for j in range(n_cols):
                if paper[i][j] == "@":
                    n_rolls = n_neighbors(paper, i, j)
                    if n_rolls < 4:
                        answer += 1
                        remove_candidates.append([i, j])
        for (i, j) in remove_candidates:
            paper[i][j] = '.'

        if len(remove_candidates) == 0:
            break

    return answer


def main():
    with open("input/input4.txt", "r") as f:
        inputs = [line.strip() for line in f.readlines()]

    print("part 1:", part1(inputs[:]))
    print("part 2:", part2(inputs[:]))

main()
