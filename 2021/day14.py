def part1(polymer_template, insertion_rules):

    for i in range(10):
        new_template = polymer_template[:]
        i = 1
        for pair_1, pair_2 in zip(polymer_template, polymer_template[1:]):
            pair = pair_1 + pair_2
            new_template.insert(i, insertion_rules[pair])
            i += 2
        #print(new_template)
        polymer_template = new_template[:]

    letter_dict = {}
    for letter in new_template:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    #print(letter_dict)
    #print(letter_dict.values())
    value = max(letter_dict.values()) - min(letter_dict.values())
    return value


import copy
def part2(polymer_template, insertion_rules):
    all_pairs, letter_dict = {}, {}
    for l in polymer_template:
        if l not in letter_dict.keys():
            letter_dict[l] = 1
        else:
            letter_dict[l] += 1
    #print(letter_dict)

    for key in insertion_rules.keys():
        all_pairs[key] = 0

    for pair_1, pair_2 in zip(polymer_template[0:-1], polymer_template[1:]):
        pair = pair_1 + pair_2
        all_pairs[pair] += 1

    new_all_pairs = copy.deepcopy(all_pairs)

    for i in range(40):
        #print(i)

        for key in all_pairs.keys():
            if all_pairs[key] != 0:
                new_pair1 = key[0] + insertion_rules[key]
                new_pair2 = insertion_rules[key] + key[1]
                new_all_pairs[new_pair1] += all_pairs[key]
                new_all_pairs[new_pair2] += all_pairs[key]
                new_all_pairs[key] -= all_pairs[key]
                if insertion_rules[key] not in letter_dict.keys():
                    letter_dict[insertion_rules[key]] = 1
                else:
                    letter_dict[insertion_rules[key]] += all_pairs[key]

        value = max(letter_dict.values()) - min(letter_dict.values())
        #print(new_all_pairs)
        #print(letter_dict)
        all_pairs = copy.deepcopy(new_all_pairs)

    return value


def main():
    with open("input/input14.txt", "r") as f:  # open file
        polymer_template, insertion_rules = [], {}
        for i, line in enumerate(f.read().splitlines()):
            if i == 0:
                polymer_template = list(line)
            if i >= 2:
                insertion_rules[line.split(' -> ')[0]] = line.split(' -> ')[1]
    #print(polymer_template)
    #print(insertion_rules)


    print("part 1:", part1(polymer_template[:], insertion_rules))
    print("part 2:", part2(polymer_template[:], insertion_rules))


main()
