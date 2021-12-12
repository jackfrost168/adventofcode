import networkx as nx


def dfs(G, node):
    if node == 'end':
        return 1

    total_value = 0
    G.nodes[node]['visited'] += 1

    for n in G.adj[node]:
        if n.isupper() or G.nodes[n]['visited'] == 0:
            total_value += dfs(G, n)

    G.nodes[node]['visited'] -= 1

    return total_value


def dfs2(G, node):
    if node == 'end':
        return 1

    total_value = 0
    G.nodes[node]['visited'] += 1

    for n in G.adj[node]:
        if n.isupper() or G.nodes[n]['visited'] == 0:
            total_value += dfs2(G, n)
        elif n != 'start' and G.nodes[n]['visited'] == 1:
            total_value += dfs(G, n)

    G.nodes[node]['visited'] -= 1

    return total_value


def main():
    G = nx.Graph()
    with open("input/input12.txt", "r") as f:  # open file
        for line in f.read().splitlines():
            line = line.strip().split('-')
            G.add_edge(line[0], line[1])
    for node in G.nodes():
        G.nodes[node]['visited'] = 0


    print("part 1:", dfs(G, 'start'))
    print("part 2:", dfs2(G, 'start'))


main()
