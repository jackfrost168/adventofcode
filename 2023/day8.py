from collections import defaultdict
import math


# Least Common Multiple
def lcm(numbers):
    ans = 1
    for x in numbers:
        ans = (x * ans) // math.gcd(x,ans)

    return ans


def part1(instructions, nodes):
    nodes_dict = defaultdict()
    for node in nodes:
        n, left, right = node.split(' ')
        nodes_dict[n] = [left, right]

    count = 0
    node = 'AAA'
    while node != 'ZZZ':
        for ins in instructions:
            if ins == 'L':
                node = nodes_dict[node][0]
            else:
                node = nodes_dict[node][1]
            count += 1

    return count


def part2(instructions, nodes):
    nodes_dict = defaultdict()
    for node in nodes:
        n, left, right = node.split(' ')
        nodes_dict[n] = [left, right]

    start_nodes = [node for node in nodes_dict.keys() if node[2] == 'A']
    nodes_nums_iter = []

    for (i, node) in enumerate(start_nodes):
        count = 0
        while node[2] != 'Z':
            for ins in instructions:
                if ins == 'L':
                    node = nodes_dict[node][0]
                else:
                    node = nodes_dict[node][1]
                count += 1

        nodes_nums_iter.append(count)

    result = lcm(nodes_nums_iter)
    #print(f"The LCM of {nums_iter} is {result}")

    return result


def main():
    with open("input/input8.txt", "r") as f:
        input = f.read().split('\n\n')
        instructions = input[0]
        nodes = input[1].split('\n')
        nodes = [node.replace(' = ', ' ').replace('(', '').replace(')', '').replace(',', '') for node in nodes]

        print('part1:', part1(instructions, nodes))
        print('part2:', part2(instructions, nodes))


main()
