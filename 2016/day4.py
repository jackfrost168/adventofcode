def part1(encrypted):
    encrypted = [line.strip().split('-') for line in encrypted]
    sum_id = 0

    for line in encrypted:
        letters = ''.join(line[0: -1])
        letter2count = {}
        for l in letters:
            if l not in letter2count.keys():
                letter2count[l] = 1
            else:
                letter2count[l] += 1

        # value decending, key ascending
        ordered = sorted(letter2count.items(), key=lambda x:(x[1],-ord(x[0])), reverse=True)
        final_key = [x[0] for x in ordered]
        checksum = ''.join(final_key)

        key = line[-1][-6: -1]
        id = int(line[-1][0:3])

        if checksum.startswith(key):
            sum_id += id

    return sum_id


def shift_cipher(letter, times):
    forward = times % 26
    new_letter = chr(ord('a') + (ord(letter) + forward - ord('a')) % 26)

    return new_letter



def part2(encrypted):

    for line in encrypted:
        code = ''
        id = int(line[-10: -7])
        for l in line:
            if l == '-':
                code += ' '
            elif '0' <= l <= '9':
                break
            else:
                l = shift_cipher(l, id)
                code += l
        if code.startswith('northpole'):
            return id


def main():
    with open("input/input4.txt", "r") as f:  # open file
        encrypted = f.readlines()  # read line, lines stores the txt file

    encrypted = [line.strip() for line in encrypted]
    print(shift_cipher('a', 52))
    ans1 = part1(encrypted[:])
    print("part 1:", ans1)
    ans2 = part2(encrypted[:])
    print("part 2:", ans2)


main()
