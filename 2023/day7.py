from collections import defaultdict


def type(strength):
    keys = list(strength.keys())
    if len(keys) == 1:
        return 'five'
    elif len(keys) == 4:
        return 'one'
    elif len(keys) == 5:
        return 'high'
    elif len(keys) == 2:
        if strength[keys[0]] == 1 or strength[keys[0]] == 4:
            return 'four'
        else:
            return 'full'
    elif len(keys) == 3:
        if strength[keys[0]] == 3 or strength[keys[1]] == 3 or strength[keys[2]] == 3:
            return 'three'
        else:
            return 'two'


def compare(card1, card2, joker=False):
    template = {'five': 7, 'four': 6, 'full': 5, 'three': 4, 'two': 3, 'one': 2, 'high': 1}
    level_strength = {7: 'five', 6: 'four', 5: 'full', 4: 'three', 3: 'two', 2: 'one', 1: 'high'}
    card2number = defaultdict()

    for (i, c) in enumerate('23456789TJQKA'):
        card2number[c] = i + 1
    if joker == True:
        card2number['J'] = 0

    strength1, strength2 = defaultdict(), defaultdict()
    for (c1, c2) in zip(card1, card2):
        if c1 in strength1.keys(): strength1[c1] += 1
        else: strength1[c1] = 1

        if c2 in strength2.keys(): strength2[c2] += 1
        else: strength2[c2] = 1

    type1, type2 = type(strength1), type(strength2)
    if joker == True:
        type1 = check_J(card1, template[type1], level_strength)
        type2 = check_J(card2, template[type2], level_strength)

    if template[type1] > template[type2]:
        return True
    elif template[type1] < template[type2]:
        return False
    else:
        for (c1, c2) in zip(card1, card2):
            if card2number[c1] < card2number[c2]:
                return False
            elif card2number[c1] > card2number[c2]:
                return True


def check_J(card, type, level_strength):
    if 'J' in card:
        num_j = 0
        for c in card:
            if c == 'J':
                num_j += 1
        if type == 1:
            if num_j == 1: return 'one'
            elif num_j == 2: return 'three'
            elif num_j == 3: return 'four'
            elif num_j == 4: return 'five'
        elif type == 2:
            return 'three'
        elif type == 3:
            if num_j == 1: return 'full'
            elif num_j == 2: return 'four'
        elif type == 4:
            if num_j == 1: return 'four'
            elif num_j == 3: return 'four'
        else:
            return 'five'
    else:
        return level_strength[type]


def part(cards_bid, joker=False):
    cards = [line[0] for line in cards_bid]
    bid = [int(line[1]) for line in cards_bid]
    card2bid = defaultdict()
    for (i, card) in enumerate(cards):
        card2bid[card] = bid[i]
    ranked = [cards[0]]

    for card in cards[1:]:
        inserted = False
        for (i, c) in enumerate(ranked):
            if compare(card, c, joker) == True:
                ranked.insert(i, card)
                inserted = True
                break
        if inserted == False:
            ranked.append(card)

    total = 0
    ranked = list(reversed(ranked))
    for (i, card) in enumerate(ranked):
        total += (i+1) * card2bid[card]

    return total


def main():
    with open("input/input7.txt", "r") as f:
        cards_bid = [line.strip().split() for line in f.readlines()]

        print('part1:', part(cards_bid[:], joker=False))
        print('part2:', part(cards_bid[:], joker=True))


main()
