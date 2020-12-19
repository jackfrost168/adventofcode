with open('input/input19.txt', 'r') as f:
    input = f.readlines()
    part = 0
    part1 = []
    part2 = []
    for line in input:
        line = line.strip()
        if len(line) == 0:
            part = 1
            continue
        if part == 0:
            part1.append(line)
        else:
            part2.append(line)
print(part1)
print(part2)

rules = {}
for line in part1:
    line = line.split(' ')
    #print(line)
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


print(rules)
import copy
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

s = find_combination(rules, 0)
print(len(s))

# ans = 0
# for line in part2:
#     if line in s:
#         ans = ans + 1
# print(ans)

# for key in rules:
#     for