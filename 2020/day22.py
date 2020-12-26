def part1(player1, player2):
    while player1 and player2:
        card_1 = player1.pop(0)
        card_2 = player2.pop(0)
        if card_1 > card_2:
            player1.append(card_1)
            player1.append(card_2)
        elif card_2 > card_1:
            player2.append(card_2)
            player2.append(card_1)

    if player1:
        winner = player1[:]
    else:
        winner = player2[:]

    score = 0
    weight = len(winner)
    for value in winner:
        score += value * weight
        weight = weight - 1
    return score


def game(player1, player2):
    appeared_player1 = set()
    appeared_player2 = set()
    while player1 and player2:
        if tuple(player1) in appeared_player1 and tuple(player2) in appeared_player2:
            return 1
        else:
            appeared_player1.add(tuple(player1))
            appeared_player2.add(tuple(player2))

        card_1 = player1.pop(0)
        card_2 = player2.pop(0)
        winner = 0
        if card_1 <= len(player1) and card_2 <= len(player2):
            winner = game(player1[0: card_1], player2[0: card_2])
        else:
            if card_1 > card_2:
                winner = 1
            elif card_1 < card_2:
                winner = 2

        if winner == 1:
            player1.append(card_1)
            player1.append(card_2)
        elif winner == 2:
            player2.append(card_2)
            player2.append(card_1)

        if len(player1) == 50 or len(player2) == 50:
            if player1:
                final_winner = player1[:]
            else:
                final_winner = player2[:]
            score = 0
            weight = len(final_winner)
            for value in final_winner:
                score += value * weight
                weight = weight - 1
            print('part2:', score)

        if player2 and not player1:
            return 2
        elif player1 and not player2:
            return 1


def main():
    with open('input/input22.txt', 'r') as f:
        player1 = []
        player2 = []
        player = 0
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('Player 1'):
                player = 1
                continue
            elif line.startswith('Player 2'):
                player = 2
                continue
            if player == 1:
                player1.append(int(line))
            elif player == 2:
                player2.append(int(line))

    ans1 = part1(player1[:], player2[:])
    print('part1:', ans1)
    winner = game(player1[:], player2[:])


main()
