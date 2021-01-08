import networkx as nx


def part1(G):
    indegree = {}
    for node in G:
        indegree[node] = G.in_degree(node)

    nodes = list(G.nodes)
    sequence = ''

    while nodes:
        for node in sorted(nodes):
            if indegree[node] == 0:
                sequence += node
                for key in G[node].keys():
                    indegree[key] -= 1
                nodes.remove(node)
                break

    return sequence


def part2(G):
    indegree = {}
    for node in G:
        indegree[node] = G.in_degree(node)

    workers = {}
    second = 0
    nodes = list(G.nodes)

    while nodes:
        for node in sorted(nodes):
            if node not in workers.keys() and indegree[node] == 0:
                if len(workers.keys()) < 5:
                    workers[node] = ord(node) - 64 + 60
                else:
                    break

        need_to_remove = []
        for node in workers.keys():
            workers[node] -= 1
            if workers[node] == 0:
                for next_node in G[node]:
                    indegree[next_node] -= 1
                nodes.remove(node)
                need_to_remove.append(node)
        for node in need_to_remove:
            del workers[node]

        second = second + 1

    return second


def main():
    with open('input/input7.txt', 'r') as f:
        G = nx.DiGraph()
        for line in f:
            line = line.strip().split(' ')
            node1, node2 = line[1], line[-3]
            G.add_edge(node1, node2)

    ans1 = part1(G)
    print('part 1:', ans1)
    ans2 = part2(G)
    print('part 2:', ans2)


main()
