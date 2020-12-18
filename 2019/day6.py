import networkx as nx

def build_graph(input):
    g = nx.DiGraph()
    for pair in input:
        if pair[0] not in g:
            g.add_node(pair[0])
        if pair[1] not in g:
            g.add_node(pair[1])
        g.add_edge(pair[1], pair[0])
    return g


def part1(g):
    ans = 0
    for node in g.nodes():
        pairs = nx.algorithms.ancestors(g, node)
        ans = ans + len(pairs)
    return ans


def part2(g):
    g = g.to_undirected()
    length = nx.shortest_path_length(g, 'YOU', 'SAN')
    length = length - 2
    return length


def main():
    with open('input/input6.txt', 'r') as f:  # open file
        input = [line.strip().split(')') for line in f.readlines()]

    #g = nx.DiGraph()
    g = build_graph(input)
    ans1 = part1(g)
    print('part1:', ans1)
    ans2 = part2(g)
    print('part2:', ans2)


main()

