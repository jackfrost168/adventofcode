def read_first_part(first_part):
    rules = {}
    for line in first_part:
        line = line.split(' ')
        if '|' in line:
            key = int(line[0][0:-1])
            rules[key] = []
            tmp_rule = []
            for i in range(1, len(line)):
                if line[i] == '|':
                    rules[key].append(tuple(tmp_rule))
                    tmp_rule = []
                    continue
                tmp_rule.append(int(line[i]))
            rules[key].append(tuple(tmp_rule))
        else:
            if '"a"' in line or '"b"' in line:
                key = int(line[0][0:-1])
                if '"a"' in line:
                    rules[key] = 'a'
                else:
                    rules[key] = 'b'
            else:
                key = int(line[0][0:-1])
                rules[key] = []
                tmp_rule = []
                for i in range(1, len(line)):
                    tmp_rule.append(int(line[i]))
                rules[key].append(tuple(tmp_rule))
    return rules


def find_combination(rules, key):
    if rules[key] == 'a':
        return 'a'
    elif rules[key] == 'b':
        return 'b'

    all_valid_messages = []
    for sub_rule in rules[key]:
        pre_valid_messages = ['']
        for rule in sub_rule:
            valid_messages = []
            s = find_combination(rules, rule)
            for pre in pre_valid_messages:
                for new in s:
                    message = pre + new
                    valid_messages.append(message)
            pre_valid_messages = valid_messages
        all_valid_messages.extend(pre_valid_messages)
    return all_valid_messages


def part1(rules, messages):
    messages_with_rule_0 = find_combination(rules, 0)
    messages_with_rule_0 = set(messages_with_rule_0)
    ans = 0
    for message in messages:
        if message in messages_with_rule_0:
            ans = ans + 1
    return ans


def matching(rules, string, rule=0, index=0):
    if index == len(string):
        return []

    rule = rules[rule]
    if type(rule) is str:
        if string[index] == rule:
            return [index + 1]
        return []

    matches = []
    for option in rule:
        sub_matches = [index]

        for sub_rule in option:
            new_matches = []
            for idx in sub_matches:
                new_matches += matching(rules, string, sub_rule, idx)
            sub_matches = new_matches

        matches += sub_matches

    return matches


def part2(rules, messages):
    valid_messages = 0

    for message in messages:
        if len(message) in matching(rules, message):
            valid_messages += 1
    return valid_messages


def main():
    with open('input/input19.txt', 'r') as f:
        part = 0
        first_part = []
        messages = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                part = 1
                continue
            if part == 0:
                first_part.append(line)
            else:
                messages.append(line)

    rules = read_first_part(first_part)

    ans1 = part1(rules, messages)
    print('part 1:', ans1)

    rules[8] = [(42,), (42, 8)]
    rules[11] = [(42, 31), (42, 11, 31)]

    ans2 = part2(rules, messages)
    print('part 2:', ans2)


main()


# from copy import deepcopy
#
#
# def parse_input(fin):
#     rules = {}
#
#     for line in map(str.rstrip, fin):
#         if not line:
#             break
#
#         rule_id, options = line.split(': ')
#         rule_id = int(rule_id)
#
#         if '"' in options:
#             rule = options[1:-1]
#         else:
#             rule = []
#             for option in options.split('|'):
#                 rule.append(tuple(map(int, option.split())))
#
#         rules[rule_id] = rule
#
#     return rules
#
#
# def match(rules, string, rule=0, index=0):
#     if index == len(string):
#         return []
#
#     rule = rules[rule]
#     if type(rule) is str:
#         if string[index] == rule:
#             return [index + 1]
#         return []
#
#     matches = []
#     for option in rule:
#         sub_matches = [index]
#
#         for sub_rule in option:
#             new_matches = []
#             for idx in sub_matches:
#                 new_matches += match(rules, string, sub_rule, idx)
#             sub_matches = new_matches
#
#         matches += sub_matches
#
#     return matches
#
#
#
# fin = open('input/input19.txt', 'r')
#
# rules1 = parse_input(fin)
# rules2 = deepcopy(rules1)
# rules2[8] = [(42,), (42, 8)]
# rules2[11] = [(42, 31), (42, 11, 31)]
# print(rules2)
# valid1 = 0
# valid2 = 0
#
# for msg in map(str.rstrip, fin):
#     if len(msg) in match(rules1, msg):
#         valid1 += 1
#     if len(msg) in match(rules2, msg):
#         valid2 += 1
#
# print(1, valid1)
# print(2, valid2)
