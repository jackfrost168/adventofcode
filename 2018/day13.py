class Cart:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.intersection_turn = -1


def solution(carts, tracks_map):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # '^>v<'
    str_dirs = '^>v<'
    first_removed = False
    while True:
        if len(carts) == 1:
            print('part 2:', '{},{}'.format(carts[0].col, carts[0].row))
            return

        crashed = []

        for cart in sorted(carts, key=lambda y: y.row*1000 + y.col):
            row, col = cart.row, cart.col  # set direction first
            face_dir = cart.direction

            if (face_dir == '^' or face_dir == 'v') and tracks_map[(row, col)] == '/':
                index_dir = ('^>v<'.index(face_dir) + 1) % 4  # make a right
                cart.direction = str_dirs[index_dir]
            elif (face_dir == '^' or face_dir == 'v') and tracks_map[(row, col)] == '\\':
                index_dir = ('^>v<'.index(face_dir) - 1) % 4  # make a left
                cart.direction = str_dirs[index_dir]
            elif (face_dir == '<' or face_dir == '>') and tracks_map[(row, col)] == '/':
                index_dir = ('^>v<'.index(face_dir) - 1) % 4  # make a left
                cart.direction = str_dirs[index_dir]
            elif (face_dir == '<' or face_dir == '>') and tracks_map[(row, col)] == '\\':
                index_dir = ('^>v<'.index(face_dir) + 1) % 4  # make a right
                cart.direction = str_dirs[index_dir]
            elif tracks_map[(row, col)] == '+':
                index_dir = ('^>v<'.index(face_dir) + cart.intersection_turn) % 4
                cart.direction = str_dirs[index_dir]
                cart.intersection_turn += 1
                if cart.intersection_turn == 2:
                    cart.intersection_turn = -1

            row_d, col_d = directions['^>v<'.index(cart.direction)]
            cart.row += row_d
            cart.col += col_d

            for other_cart in carts:
                if other_cart != cart and other_cart.row == cart.row and other_cart.col == cart.col:
                    if first_removed is False:
                        print('part 1:', '{},{}'.format(cart.col, cart.row))
                        first_removed = True
                    crashed.append(cart)
                    crashed.append(other_cart)

        for crash in crashed:
            carts.remove(crash)


def main():
    with open('input/input13.txt', 'r') as f:
        tracks_map = {}
        carts = []
        for i, line in enumerate(f):
            for j, track in enumerate(line.strip('\n')):
                if track == ' ':
                    continue
                if track == '^' or track == 'v':
                    tracks_map[(i, j)] = '|'
                    carts.append(Cart(i, j, track))
                elif track == '<' or track == '>':
                    tracks_map[(i, j)] = '-'
                    carts.append(Cart(i, j, track))
                else:
                    tracks_map[(i, j)] = track

    solution(carts, tracks_map)


main()
