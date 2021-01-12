with open('input/input16.txt', 'r') as f:
    f = f.readlines()
    i = 0
    samples = {}  # [before, instruction, after]
    id = 0
    part = 1
    instructions = []
    while i < len(f):
        if part == 1:
            before = f[i].strip().replace('Before: [', '').replace(']', '').split(',')
            before = [int(num) for num in before]
            instruction = f[i+1].strip().split(' ')
            instruction = [int(num) for num in instruction]
            after = f[i+2].strip().replace('After:  [', '').replace(']', '').split(',')
            after = [int(num) for num in after]
            samples[id] = [before, instruction, after]

            id = id + 1
            i = i + 4
            if len(f[i].strip()) == 0:
                part = 2
                i = i + 2
        else:
            instruction = [int(num) for num in f[i].strip().split(' ')]
            instructions.append(instruction)
            i = i + 1

print(samples)
print(instructions)

def valid_epcode(before, instruction):
    register_value1, register_value2 = before[instruction[1]], before[instruction[2]]
    immediate_value1, immediate_value2 = instruction[1], instruction[2]
    output_pos = instruction[3]

    addr = before[:]
    value = register_value1 + register_value2
    addr[output_pos] = value

    addi = before[:]
    value = register_value1 + immediate_value2
    addi[output_pos] = value

    mulr = before[:]
    value = register_value1 * register_value2
    mulr[output_pos] = value

    muli = before[:]
    value = register_value1 * immediate_value2
    muli[output_pos] = value

    banr = before[:]
    value = register_value1 & register_value2
    banr[output_pos] = value

    bani = before[:]
    value = register_value1 & immediate_value2
    bani[output_pos] = value

    borr = before[:]
    value = register_value1 | register_value2
    borr[output_pos] = value

    bori = before[:]
    value = register_value1 | immediate_value2
    bori[output_pos] = value

    setr = before[:]
    setr[output_pos] = register_value1

    seti = before[:]
    seti[output_pos] = immediate_value1

    gtir = before[:]
    value = 1 if immediate_value1 > register_value2 else 0
    gtir[output_pos] = value

    gtri = before[:]
    value = 1 if register_value1 > immediate_value2 else 0
    gtri[output_pos] = value

    gtrr = before[:]
    value = 1 if register_value1 > register_value2 else 0
    gtrr[output_pos] = value

    eqir = before[:]
    value = 1 if immediate_value1 == register_value2 else 0
    eqir[output_pos] = value

    eqri = before[:]
    value = 1 if register_value1 == immediate_value2 else 0
    eqri[output_pos] = value

    eqrr = before[:]
    value = 1 if register_value1 == register_value2 else 0
    eqrr[output_pos] = value

    return [addr, addi, mulr, muli, banr, bani, borr, bori,
            setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    # if [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti,
    #     gtir, gtri, gtrr, eqir, eqri, eqrr].count(after) >= 3:
    #     return True
    # else:
    #     return False

ans = 0
instruction_map = {}
for key in samples.keys():
    before = samples[key][0]
    instruction = samples[key][1]
    after = samples[key][2]
    all_afters = valid_epcode(before, instruction)
    if all_afters.count(after) >= 3:
        ans += 1
print(ans)

before = instructions[0]
for instruction in instructions:
    all_afters = valid_epcode(before, instruction)
    after = all_afters[instruction[0]]
    before = after[:]

print(before)

