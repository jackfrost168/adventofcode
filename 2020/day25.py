def get_loop_size(public_key):
    subject_number = 7
    value = 1
    loop_size = 0
    while value != public_key:
        value = value * subject_number
        value = value % 20201227
        loop_size += 1

    return loop_size


def main():
    with open('input/input25.txt', 'r') as f:
        f = f.readlines()
        card_public_key = int(f[0].strip())
        door_public_key = int(f[1].strip())

    card_loop_size = get_loop_size(card_public_key)
    door_loop_size = get_loop_size(door_public_key)

    print('part1:', pow(door_public_key, card_loop_size, 20201227))
    print('part1:', pow(card_public_key, door_loop_size, 20201227))


main()
