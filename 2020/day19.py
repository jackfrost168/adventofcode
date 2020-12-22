def read_input(first_part, second_part):
    rules = {}
    for line in first_part:
        line = line.split(' ')
        if '|' in line:
            key = int(line[0][0:-1])
            rules[key] = []
            tmp_rule = []
            for i in range(1, len(line)):
                if line[i] == '|':
                    rules[key].append(tmp_rule)
                    tmp_rule = []
                    continue
                tmp_rule.append(line[i])
            rules[key].append(tmp_rule)
        else:
            if '"a"' in line or '"b"' in line:
                key = int(line[0][0:-1])
                if '"a"' in line:
                    rules[key] = ['a']
                else:
                    rules[key] = ['b']
            else:
                key = int(line[0][0:-1])
                rules[key] = []
                tmp_rule = []
                for i in range(1, len(line)):
                    tmp_rule.append(line[i])
                rules[key].append(tmp_rule)
    return rules, second_part


def find_combination(rules, key):
    if rules[key] == ['a']:
        return 'a'
    elif rules[key] == ['b']:
        return 'b'

    final_rules = []
    for sub_rule in rules[key]:
        pre_rule = ['']
        for rule in sub_rule:
            strings = []
            s = find_combination(rules, int(rule))
            for pre in pre_rule:
                for new in s:
                    string = pre + new
                    strings.append(string)
            pre_rule = strings
        final_rules.extend(pre_rule)
    return final_rules

def part1(rules, messages):
    rule_0 = find_combination(rules, 0)
    rule_0 = set(rule_0)
    ans = 0
    for message in messages:
        if message in rule_0:
            ans = ans + 1
    return ans


def main():
    with open('input/input19.txt', 'r') as f:
        input = f.readlines()
        part = 0
        first_part = []
        second_part = []
        for line in input:
            line = line.strip()
            if len(line) == 0:
                part = 1
                continue
            if part == 0:
                first_part.append(line)
            else:
                second_part.append(line)

    rules, messages = read_input(first_part, second_part)
    ans1 = part1(rules, messages)
    print('part1:', ans1)


main()
