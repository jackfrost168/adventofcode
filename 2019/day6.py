import networkx as nx


def build_graph(orbits):
    G = nx.DiGraph()
    for pair in orbits:
        if pair[0] not in G:
            G.add_node(pair[0])
        if pair[1] not in G:
            G.add_node(pair[1])
        G.add_edge(pair[1], pair[0])
    return G


def part1(G):
    ans = 0
    for node in G.nodes():
        pairs = nx.algorithms.ancestors(G, node)
        ans = ans + len(pairs)
    return ans


def part2(G):
    G = G.to_undirected()
    length = nx.shortest_path_length(G, 'YOU', 'SAN')
    length = length - 2
    return length


def main():
    with open('input/input6.txt', 'r') as f:  # open file
        orbits = [line.strip().split(')') for line in f]

    G = build_graph(orbits)
    ans1 = part1(G)
    print('part 1:', ans1)
    ans2 = part2(G)
    print('part 2:', ans2)


main()
