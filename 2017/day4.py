def part1(passphrases):
    num_valid = 0
    for passphrase in passphrases:
        vaild = 1
        valid_words = []
        for word in passphrase:
            if word not in valid_words:
                valid_words.append(word)
            else:
                vaild = 0
                break
        num_valid += vaild
    return num_valid


def part2(passphrases):
    num_valid = 0
    for passphrase in passphrases:
        vaild = 1
        valid_words = []
        for word in passphrase:
            word = sorted(word)
            if word not in valid_words:
                valid_words.append(word)
            else:
                vaild = 0
                break
        num_valid += vaild
    return num_valid


def main():
    with open('input/input4.txt', 'r') as f:
        f = f.readlines()
    passphrases = []
    for line in f:
        line = line.strip().split()
        passphrases.append(line)

    answer1 = part1(passphrases)
    print('part1:', answer1)
    answer2 = part2(passphrases)
    print('part2:', answer2)


main()
