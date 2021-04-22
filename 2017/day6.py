def part(memory):
    cycles = 0
    showed = []
    while memory not in showed:
        showed.append(memory[:])
        max_blocks = max(memory)
        id = memory.index(max_blocks)
        memory[id] = 0
        while max_blocks > 0:
            id += 1
            if id == len(memory):
                id = 0
            memory[id] += 1
            max_blocks -= 1
        if memory in showed:
            before_id = showed.index(memory)
        cycles += 1
    loops = cycles - before_id
    return cycles, loops


def main():
    with open('input/input6.txt', 'r') as f:
        memory = [int(num) for num in f.read().split()]
    cycles, loops = part(memory[:])
    print('part1:', cycles)
    print('part2:', loops)


main()
