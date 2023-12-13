import itertools
from functools import lru_cache


# def check_match(spring, config):
#     spring = ''.join(spring)
#     spring = spring.replace('.', ' ').split()
#
#     if len(spring) == len(config):
#         for s, conf in zip(spring, config):
#             if len(s) != conf:
#                 return False
#         return True
#     else:
#         return False
#
#
# def part1(springs, configs):
#     total = 0
#     for (spring, config) in zip(springs, configs):
#         count_config = 0
#         spring = list(spring)
#         num_unknown = spring.count('?')
#         all_possible = list(itertools.product(['.', '#'], repeat=num_unknown))
#         for possible in all_possible:
#             update_spring = spring[:]
#             start = 0
#             for (i, s) in enumerate(update_spring):
#                 if update_spring[i] == '?':
#                     update_spring[i] = possible[start]
#                     start += 1
#
#             is_match = check_match(update_spring, config)
#             if is_match == True:
#                 count_config += 1
#
#         total += count_config
#
#     return total


def solution(springs, configs, fold=1):
    total = 0
    for (spring, config) in zip(springs, configs):
        spring = '?'.join([spring] * fold)
        config = config * fold

        @lru_cache
        def dp(s, c, r=0):
            if s >= len(spring):
                return c == len(config)
            if spring[s] in '?.':
                r += dp(s + 1, c)
            if c == len(config):
                return r

            if spring[s] in '?#' and \
                    (s + config[c] <= len(spring) and '.' not in spring[s:s + config[c]]) and \
                    (s + config[c] == len(spring) or spring[s + config[c]] != '#'):
                r += dp(s + config[c] + 1, c + 1)

            return r

        total += dp(0, 0)

    return total


def main():
    with open('input/input12.txt') as f:
        springs, configs = [], []
        for line in f.readlines():
            spring, config = line.strip().split()
            springs.append(spring)
            configs.append(list(map(int, config.split(','))))

    print('part1:', solution(springs, configs, 1))
    print('part2:', solution(springs, configs, 5))


main()
