class Node:  # double circular linked list
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


def part1(players, last_worth):
    marbles = [0]
    current_pos = 0
    scores = {}
    for i in range(1, last_worth+1):
        if i % 23 != 0:
            current_pos = (current_pos + 2) % len(marbles)
            marbles.insert(current_pos, i)
        else:
            current_pos = (current_pos - 7) % len(marbles)
            player = (i-1) % players + 1
            remove_score = marbles.pop(current_pos)
            if player not in scores.keys():
                scores[player] = remove_score + i
            else:
                scores[player] += remove_score + i

    highest_score = max([scores[player] for player in scores.keys()])

    return highest_score


def part2(players, last_worth):
    current = Node(0)
    current.next = current
    current.pre = current
    scores = {}
    for i in range(1, last_worth+1):
        if i % 23 != 0:
            current = current.next

            tmp = Node(i)  # insert node in double circular linked list
            tmp.next = current.next
            current.next.pre = tmp
            current.next = tmp
            tmp.pre = current

            current = current.next
        else:
            for _ in range(8):
                current = current.pre
            tmp = current.next
            current.next = tmp.next
            tmp.next.pre = current
            tmp.next, tmp.pre = None, None

            current = current.next
            player = (i-1) % players + 1
            remove_score = tmp.value
            if player not in scores.keys():
                scores[player] = remove_score + i
            else:
                scores[player] += remove_score + i

        # if i % 10000 == 0:
        #     print(i)

    highest_score = max([scores[player] for player in scores.keys()])

    return highest_score


def main():
    with open('input/input9.txt', 'r') as f:
        f = f.read().strip().split(' ')
        last_worth = int(f[-2])
        players = int(f[0])

    ans1 = part1(players, last_worth)
    print('part 1:', ans1)
    ans2 = part2(players, last_worth * 100)  # about half minute
    print('part 2:', ans2)


main()
