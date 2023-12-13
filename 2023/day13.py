def check_reflection(mirror, error=0):
    for row in range(len(mirror)-1):
        row_up, row_down = row, row + 1
        diff = 0
        while row_up >= 0 and row_down <= len(mirror)-1:
            diff += sum([0 if p1 == p2 else 1 for (p1, p2) in zip(mirror[row_up], mirror[row_down])])
            row_up = row_up - 1
            row_down = row_down + 1
        if diff == error:
            return True, row + 1

    return False, -1


def solution(mirrors, error=1):
    total = 0
    for mirror in mirrors:
        transpose_mirror = list(map(list, zip(*mirror)))
        reflection, row = check_reflection(mirror, error)
        if reflection == True:
            total += row * 100
            continue
        reflection, col = check_reflection(transpose_mirror, error)
        if reflection == True:
            total += col

    return total


def main():
    with open('input/input13.txt') as f:
        tables = f.read().split('\n\n')
        mirrors = [[list(line) for line in table.strip().split('\n')] for table in tables]

    print('part1:', solution(mirrors[:], 0))
    print('part2:', solution(mirrors[:], 1))

main()


# def transpose_2d(data):
#     # transposed = list(zip(*data))
#     # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
#     # 注意 zip 本身返回的数据类型为 tuple 元组
#     # 其中符号 * 号可以对元素进行解压或展开
#
#     transposed = list(map(list, zip(*data)))
#     return transposed
#
#
# data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print([a for a in zip(*data)])
# print(transpose_2d(data))