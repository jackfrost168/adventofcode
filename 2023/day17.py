from heapq import heappop, heappush


def solution(input, move=1, maximum=3):
    costs = {}
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = [(0, 0, 0, -1)]
    seen = set()
    while q:
        cost, i, j, direction = heappop(q)
        if i == len(input)-1 and j == len(input[0]) - 1:
            return cost
        if (i, j, direction) in seen:
            continue
        seen.add((i, j, direction))
        for d in range(4):
            if d == direction or (d + 2) % 4 == direction:
                continue
            cost_increase = 0
            for dis in range(1, maximum+1):
                new_i = i + dir[d][0] * dis
                new_j = j + dir[d][1] * dis
                if 0 <= new_i <= len(input)-1 and 0 <= new_j <= len(input[0])-1:
                    cost_increase += input[new_i][new_j]
                    if dis < move:
                        continue
                    new_cost = cost + cost_increase
                    if costs.get((new_i, new_j, d), 1e100) <= new_cost:
                        continue
                    costs[(new_i, new_j, d)] = new_cost
                    heappush(q, (new_cost, new_i, new_j, d))


def main():
    with open('input/input17.txt') as f:
        input = [[int(i) for i in line.strip()] for line in f.readlines()]

        print('part1:', solution(input[:], move=1, maximum=3))
        print('part2:', solution(input[:], move=4, maximum=10))


main()
