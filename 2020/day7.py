import networkx as nx

def part1(G, target):
    ancestors = nx.algorithms.ancestors(G, target)
    return len(ancestors)


def part2(G, target):
    for node in nx.dfs_postorder_nodes(G, target):
        cur_weight = 0
        for (contain_bag, bag_to_contain) in G[node].items():
            cur_weight += bag_to_contain['weight'] * (G.nodes[contain_bag]['weight'] + 1)
        G.nodes[node]["weight"] = cur_weight

    return G.nodes["shiny gold"]['weight']


def main():
    with open('input/input7.txt') as f:
        G = nx.DiGraph()

        for line in f:
            bag, contains = line.strip().rstrip(".").split(" bags contain ")

            if contains == "no other bags":
                continue

            for other_bag in contains.split(", "):
                count = int(other_bag[0])
                other_bag = other_bag[2:].rstrip("bags").strip()
                G.add_edge(bag, other_bag, weight=count)

    ancestors = part1(G, 'shiny gold')
    print('part 1:', ancestors)
    total_bags = part2(G, 'shiny gold')
    print('part 2:', total_bags)


main()


# f = open("input/input7.txt", "r") #open file
# lines = f.readlines()        #read line, lines stores the txt file
# input = []
# bags = {}
# bags_num = {}
# for line in lines:
#     line = line.strip('\n').strip('.').replace(',', '') #take away '\n'
#     line = line.split(' ')
#     #print(line)
#     string = ''
#     head = True
#     key = ''
#     for i in range(len(line)):
#         if line[i] != 'contain' and (line[i] < '0' or line[i] > '9'):
#             if (line[i] != 'bag' and line[i] != 'bags'):
#                 string = string + line[i] + ' '
#             elif (line[i] == 'bag' or line[i] == 'bags'):
#                 if head == True:
#                     string = string.strip(' ')
#                     bags[string] = []
#                     key = string
#                     string = ''
#                     head = False
#                 else:
#                     string = string.strip(' ')
#                     bags[key].append(string)
#                     string = ''
#
# #print(bags)
# ans = 0
#
# import networkx as nx
# G = nx.DiGraph()
# for key in bags.keys():
#     values = bags[key]
#     G.add_node(key)
#     for value in values:
#         if value != 'no other':
#             G.add_node(value)
#             G.add_edge(key, value)
#
# a = nx.algorithms.ancestors(G, 'shiny gold')
# print(len(a))
#
# b = nx.algorithms.descendants(G, 'shiny gold')
