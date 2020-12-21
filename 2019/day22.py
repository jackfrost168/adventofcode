num_cards = 10007

def cut_cards(deck, N):
    pos = N % num_cards
    first_part = deck[0 : pos]
    second_part = deck[pos:]
    cut_deck = second_part + first_part
    return cut_deck

def deal_into_stack(deck):
    shuffled_deck = list(reversed(deck))
    return shuffled_deck

def deal_increment_cards(deck, N):
    pos = N % num_cards
    shuffled_deck = [0 for i in range(num_cards)]
    i = 0
    for card in deck:
        shuffled_deck[i] = card
        i = i + pos
        if i > len(deck):
            i = i % num_cards
    return shuffled_deck

def part1(shuffle_techniques):
    deck = [i for i in range(num_cards)]
    for technique, N in shuffle_techniques:
        if technique == 'cut':
            deck = cut_cards(deck, N)
        elif technique == 'deal_into':
            deck = deal_into_stack(deck)
        elif technique == 'deal_increment':
            deck = deal_increment_cards(deck, N)

    return deck.index(2019)


def part2(shuffle_techniques):
    cards = 119315717514047
    times = 101741582076661

    a = 1
    b = 0
    for technique, N in shuffle_techniques:

        if technique == 'cut':
            new_a, new_b = 1, -1*N
        elif technique == 'deal_into':
            new_a, new_b = -1, -1
        elif technique == 'deal_increment':
            new_a, new_b = N, 0

        a = (new_a * a) % cards
        b = (new_a * b + new_b) % cards

    ra = pow(a, times, cards)
    rb = (b * (ra - 1) * pow(a - 1, cards-2, cards)) % cards
    #print("Part 2:", (2020 - rb) * pow(ra, cards-2, cards) % cards)
    return (2020 - rb) * pow(ra, cards-2, cards) % cards


def main():
    with open('input/input22.txt', 'r') as f:
        f = f.readlines()
        input = [line.strip() for line in f]
        shuffle_techniques = []
        for line in input:
            line = line.split(' ')
            if line[0] == 'cut':
                shuffle_techniques.append((line[0], int(line[1])))
            elif line[1] == 'with':
                shuffle_techniques.append(('deal_increment', int(line[-1])))
            else:
                shuffle_techniques.append(('deal_into', 0))

    ans1 = part1(shuffle_techniques)
    print('part1:', ans1)
    ans2 = part2(shuffle_techniques)
    print('part2:', ans2)


main()
