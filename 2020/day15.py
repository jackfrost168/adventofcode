def record_appeared(appeared_num, age, turn):
    if age not in appeared_num.keys():
        appeared_num[age] = [turn + 1]
    else:
        appeared_num[age].append(turn + 1)
        if len(appeared_num[age]) > 2:
            appeared_num[age].pop(0)


def solution(input, stop_turn):
    turn = 0
    appeared_num = {}
    last_num = 0
    while turn < stop_turn:
        if turn < len(input):
            last_num = input[turn]
            starting_num = input[turn]
            record_appeared(appeared_num, starting_num, turn)
        else:
            if len(appeared_num[last_num]) == 1:
                last_num = 0
                record_appeared(appeared_num, 0, turn)
            else:
                turn1 = appeared_num[last_num][0]
                turn2 = appeared_num[last_num][1]
                age = abs(turn1 - turn2)
                last_num = age
                record_appeared(appeared_num, age, turn)
        turn = turn + 1
        # if turn % 1000000 == 0:
        #     print(turn)
    return last_num


def main():
    f = open('input15.txt').read()
    f = f.strip('\n').split(',')
    input = [int(s) for s in f]  # input = [6,19,0,5,7,13,1]

    ans1 = solution(input, 2020)
    print('part1:', ans1)
    ans2 = solution(input, 30000000)
    print('part2:', ans2)


main()