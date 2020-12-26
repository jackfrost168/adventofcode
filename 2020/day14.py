def str_decimal_to_bin(value, length):
    str_bin_value = bin(value)
    str_bin_value = str(str_bin_value)[2:]
    while len(str_bin_value) < length:
        str_bin_value = '0' + str_bin_value
    return str_bin_value


def part1(masks):
    memory = {}
    for key in masks.keys():
        mask = key
        for i in range(0, len(masks[key])):
            address = masks[key][i][0]
            value = masks[key][i][1]
            str_bin_value = str_decimal_to_bin(value, len(mask))
            j = len(mask) - 1
            str_new_value = ''
            while j >= 0:
                if mask[j] == '1' or mask[j] == '0':
                    str_new_value = mask[j] + str_new_value
                else:
                    str_new_value = str_bin_value[j] + str_new_value
                j = j - 1
            memory[address] = str_new_value

    ans = 0
    for key in memory:
        value = memory[key]
        ans = ans + int(value, 2)

    return ans


def part2(masks):
    memory = {}
    for key in masks.keys():
        mask = key
        for i in range(0, len(masks[key])):
            address = masks[key][i][0]
            value = masks[key][i][1]
            bin_address = str_decimal_to_bin(address, len(mask))
            j = len(mask) - 1
            str_new_adderss = ''
            while j >= 0:
                if mask[j] == '0':
                    str_new_adderss = bin_address[j] + str_new_adderss
                elif mask[j] == '1':
                    str_new_adderss = '1' + str_new_adderss
                elif mask[j] == 'X':
                    str_new_adderss = 'X' + str_new_adderss
                j = j - 1

            num_X = 0
            for s in str_new_adderss:
                if s == 'X':
                    num_X = num_X + 1

            if num_X > 0:
                length = pow(2, num_X)
                for m in range(length):
                    str_new_address = list(str_new_adderss)
                    cur_ = str_decimal_to_bin(m, num_X)
                    pos_cur = 0
                    for n in range(len(str_new_adderss)):
                        if str_new_address[n] == 'X':
                            str_new_address[n] = str(cur_[pos_cur])
                            pos_cur = pos_cur + 1
                    str_new_address = ''.join(str_new_address)
                    memory[str_new_address] = value
            else:
                memory[str_new_adderss] = value

    ans = 0
    for key in memory:
        value = memory[key]
        ans = ans + value

    return ans


def main():
    with open('input/input14.txt', 'r') as f:
        masks = {}
        i = 0
        mask = ''
        for line in f:
            if line.startswith('mask'):
                line = line.strip('\n')
                line = line.split('=')
                mask = line[1].strip(' ')
                masks[mask] = []
                i = i + 1
            else:
                line = line.strip('\n')
                line = line.split('=')
                address = int(line[0][4:-2])
                value = int(line[1])
                masks[mask].append((address, value))

    ans1 = part1(masks)
    print('part1:', ans1)
    ans2 = part2(masks)
    print('part2:', ans2)


main()
