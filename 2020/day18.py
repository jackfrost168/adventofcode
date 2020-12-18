def part1(input):
    ans = 0
    for line in input:
        stack = []
        operator = []
        for s in line:
            if s in '+*()':
                operator.append(s)
                if operator[-1] == ')':
                    operator.pop()
                    operator.pop()
                    if len(operator) != 0 and operator[-1] != '(' and operator[-1] != ')':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        oper = operator.pop()
                        if oper == '+':
                            stack.append(int(num1) + int(num2))
                        elif oper == '*':
                            stack.append(int(num1) * int(num2))
            else:
                stack.append(s)
                if len(operator) != 0 and operator[-1] != '(' and operator[-1] != ')':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    oper = operator.pop()
                    if oper == '+':
                        stack.append(int(num1) + int(num2))
                    elif oper == '*':
                        stack.append(int(num1) * int(num2))
        ans = ans + stack[0]
    return ans


def precede(operator1, operator2):
    if operator1 == '(':
        if operator2 == ')':
            return '='
        else:
            return '<'
    elif operator1 == ')':
        return '>'
    elif operator1 == '+':
        if operator2 == '*' or operator2 == ')' or operator2 == '+' or operator2 == '#':
            return '>'
        elif operator2 == '(':
            return '<'
    elif operator1 == '*':
        if operator2 == '*' or operator2 == ')' or operator2 == '#':
            return '>'
        elif operator2 == '+' or operator2 == '(':
            return '<'
    elif operator1 == '#':
        if operator2 == '#':
            return '='
        else:
            return '<'


def part2(input):
    ans = 0
    for line in input:
        line.append('#')
        stack = []
        operator = ['#']
        c = line[0]
        i = 0
        while i < len(line) and c != '#':
            #c = line[i]
            while c != '#' or operator[-1] != '#':
                if c not in '+*()#':
                    stack.append(c)
                    i = i + 1
                    c = line[i]
                else:
                    priority = precede(operator[-1], c)
                    if priority == '<':
                        operator.append(c)
                        i = i + 1
                        c = line[i]
                        continue
                    elif priority == '=':
                        operator.pop()
                        i = i + 1
                        c = line[i]
                        continue
                    elif priority == '>':
                        oper = operator.pop()
                        num1 = stack.pop()
                        num2 = stack.pop()
                        if oper == '+':
                            stack.append(int(num1) + int(num2))
                        elif oper == '*':
                            stack.append(int(num1) * int(num2))
                        continue

        ans = ans + stack[0]
    return ans

def main():
    with open('input/input18.txt') as f:
        f = [line.strip().split(' ') for line in f]
    input = []
    for line in f:
        tmp_line = []
        for s in line:
            if len(s) == 1:
                tmp_line.append(s)
            else:
                for ss in s:
                    tmp_line.append(ss)
        input.append(tmp_line)
    # print(input)
    ans1 = part1(input)
    print('part1:', ans1)
    ans2 = part2(input)
    print('part2:', ans2)


main()


