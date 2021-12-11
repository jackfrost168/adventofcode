def part1(subsystem):
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    errors = 0
    for line in subsystem:
        stack = []
        for s in line:
            if s in '([{<':
                stack.append(s)
            else:
                bracket = stack[-1] + s
                if bracket in ['()', '[]', '{}', '<>']:
                    stack.pop()
                else:
                    errors += score[s]
                    break

    return errors


def part2(subsystem):
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    errors = 0
    corrupted = subsystem[:]
    for line in subsystem:
        stack = []
        for s in line:
            if s in '([{<':
                stack.append(s)
            else:
                bracket = stack[-1] + s
                if bracket in ['()', '[]', '{}', '<>']:
                    stack.pop()
                else:
                    errors += score[s]
                    corrupted.remove(line)
                    break

    stacks = []
    for line in corrupted:
        stack = []
        for s in line:
            if s in '([{<':
                stack.append(s)
            else:
                stack.pop()
        stacks.append(stack)

    completes = []
    for stack in stacks:
        complete = ''
        for s in stack:
            if s == '(': complete = ')' + complete
            elif s == '[': complete = ']' + complete
            elif s == '{': complete = '}' + complete
            elif s == '<': complete = '>' + complete
        completes.append(complete)

    table = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for complete in completes:
        score = 0
        for s in complete:
            score = score * 5 + table[s]

        scores.append(score)

    scores = sorted(scores)

    return scores[len(scores)//2]


def main():
    with open("input/input10.txt", "r") as f:  # open file
        subsystem = [line.strip() for line in f.read().splitlines()]

    print("part 1:", part1(subsystem[:]))
    print("part 2:", part2(subsystem[:]))


main()
