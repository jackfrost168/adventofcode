def part1(player1, player2):
    while player1 and player2:
        card_1 = player1.pop(0)
        card_2 = player2.pop(0)
        if card_1 > card_2:
            player1.append(card_1)
            player1.append(card_2)
        elif card_1 < card_2:
            player2.append(card_2)
            player2.append(card_1)

    #print('player1:', player1)
    #print('player2:', player2)

    ans = 0
    weight = len(player1)
    for i in range(len(player1)):
        s = player1[i] * weight
        ans = ans + s
        weight = weight - 1
    return ans

def game(player1, player2):
    #print('player1:', player1)
    #print('player2:', player2)
    appeared_player1 = []
    appeared_player2 = []
    while player1 and player2:
        if tuple(player1) in appeared_player1 and tuple(player2) in appeared_player2:
            #print('loop')
            return 1
        else:
            appeared_player1.append(tuple(player1))
            appeared_player2.append(tuple(player2))

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
        if (len(player1) == 50 and len(player2) == 0) or \
                (len(player2) == 50 and len(player1) == 0):
            #print('part2: player1,', player1)
            #print('part2: player2,', player2)
            ans = 0
            weight = len(player1)
            for i in range(len(player1)):
                s = player1[i] * weight
                ans = ans + s
                weight = weight - 1
            print('part2:', ans)
            ans = 0
            weight = len(player2)
            for i in range(len(player2)):
                s = player2[i] * weight
                ans = ans + s
                weight = weight - 1
            #print('ans_player2:', ans)
        if len(player1) == 0 and len(player2) != 0:
            return 2
        elif len(player1) != 0 and len(player2) == 0:
            return 1


def main():
    with open('input/input22.txt', 'r') as f:
        f = f.readlines()
        player1 = []
        player2 = []
        player = 0
        for line in f:
            line = line.strip()
            if len(line) == 0:
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
    #print(len(player1), len(player2))
    #print(player1)
    #print(player2)

    ans1 = part1(player1[:], player2[:])
    print('part1:', ans1)
    winner = game(player1[:], player2[:])

main()
