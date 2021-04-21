import copy


def part1(initial_state, minutes):
    state = copy.deepcopy(initial_state)
    time = 0
    while time < minutes:
        state_copy = copy.deepcopy(state)
        for i in range(len(state)):
            for j in range(len(state[0])):
                num_open, num_wooded, num_lumberyard = 0, 0, 0
                for m in [-1, 0, 1]:
                    for n in [-1, 0, 1]:
                        if 0 <= i + m < len(state) and 0 <= j + n < len(state[0]):
                            if m == n == 0:
                                continue
                            if state[i+m][j+n] == '.':
                                num_open += 1
                            elif state[i+m][j+n] == '|':
                                num_wooded += 1
                            elif state[i+m][j+n] == '#':
                                num_lumberyard += 1
                if state[i][j] == '.':
                    if num_wooded >= 3:
                        state_copy[i][j] = '|'
                if state[i][j] == '|':
                    if num_lumberyard >= 3:
                        state_copy[i][j] = '#'
                if state[i][j] == '#':
                    if not (num_lumberyard >= 1 and num_wooded >= 1):
                        state_copy[i][j] = '.'
        state = copy.deepcopy(state_copy)
        time = time + 1

    return state


def wooded_mult_lumberyard(state):
    wooded, lumberyard = 0, 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '|':
                wooded += 1
            elif state[i][j] == '#':
                lumberyard += 1
    return wooded * lumberyard


def main():
    with open('input/input18.txt', 'r') as f:
        f = f.readlines()
        initial_state = []
        for line in f:
            line = [c for c in line.strip()]
            initial_state.append(line)
    state1 = part1(initial_state, 10)
    answer1 = wooded_mult_lumberyard(state1)
    print('part1:', answer1)
    state2 = part1(initial_state, (1000000000 - 600) % 28 + 600)
    answer2 = wooded_mult_lumberyard(state2)
    print('part2:', answer2)


main()
