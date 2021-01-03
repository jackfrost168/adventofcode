def part1(rules, initial_state):
    old_state = initial_state[:]
    generation = 0
    while generation < 20:  # while generation < 5000
        old_state = ['.', '.', '.'] + old_state + ['.', '.', '.']
        new_state = old_state[:]
        for i in range(2, len(old_state)-2):
            LLCRR = ''.join(old_state[i-2: i+3])
            new_state[i] = rules[LLCRR]

        old_state = new_state[:]
        generation += 1

    total_pots = 0
    for i, pot in enumerate(old_state):
        if pot == '#':
            total_pots += i - generation * 3

    return total_pots


def main():
    with open('input/input12.txt', 'r') as f:
        rules = {}  # {'##.#.': '.', '##.##': '.'}
        for line in f:
            line = line.strip()
            if line.startswith('initial state'):
                line = line.replace('initial state: ', '')
                initial_state = list(line)
                continue
            if len(line) != 0:
                line = line.replace(' => ', ' ')
                line = line.split(' ')
                rules[line[0]] = line[1]

    total_pots = part1(rules, initial_state[:])
    print('part 1:', total_pots)
    # After 1000 generation is liner growth by 80.
    # That means the answer of 1000 generation is 80000, 2000 generation is 16000 et al.
    print('part 2:', 50000000000 // 1000 * 80000)


main()
