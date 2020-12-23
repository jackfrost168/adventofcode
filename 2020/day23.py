def part1(nums, moves):
    m = 0
    while m < moves:
        current = nums[0]
        first, second, third = nums[1:4]
        nums.pop(1)
        nums.pop(1)
        nums.pop(1)
        dest_cup = current - 1
        if dest_cup == 0:
            dest_cup = 9
        while dest_cup not in nums:
            dest_cup = dest_cup - 1
            if dest_cup == 0:
                dest_cup = 9
        des_index = nums.index(dest_cup)
        nums.insert(des_index + 1, first)
        nums.insert(des_index + 2, second)
        nums.insert(des_index + 3, third)

        nums = nums[1:] + nums[0:1]
        m = m + 1

    index_1 = nums.index(1)
    ans = nums[index_1+1:] + nums[0: index_1]
    ans = [str(s) for s in ans]
    return ''.join(ans)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def part2(nums, moves):
    nodes = [Node(value) for value in nums]
    nodes[0].prev = nodes[-1]
    nodes[0].next = nodes[1]
    nodes[len(nodes)-1].next = nodes[0]
    nodes[len(nodes)-1].prev = nodes[len(nodes) - 2]
    for i in range(1, len(nodes)-1):
        nodes[i].next = nodes[i+1]
        nodes[i].prev = nodes[i-1]

    value_pos = {}
    for i, value in enumerate(nums):
        value_pos[value] = i

    cups_length = len(nums)
    current = nodes[0]
    m = 0
    while m < moves:
        first = current.next
        second = current.next.next
        third = current.next.next.next

        dest_cup = current.value - 1
        if dest_cup == 0:
            dest_cup = cups_length
        while dest_cup == first.value or dest_cup == second.value or dest_cup == third.value:
            dest_cup = dest_cup - 1
            if dest_cup == 0:
                dest_cup = cups_length
        dest_index = value_pos[dest_cup]

        current.next = third.next
        third.next.prev = current

        third.next = nodes[dest_index].next
        nodes[dest_index].next.prev = third

        nodes[dest_index].next = first
        first.prev = nodes[dest_index]

        current = current.next
        m = m + 1

    id_1 = value_pos[1]
    return nodes[id_1].next.value*nodes[id_1].next.next.value


def main():
    with open('input/input23.txt', 'r') as f:
        f = f.read().strip()   #f = '942387615'

    nums = [int(s) for s in f]
    ans1 = part1(nums[:], 100)
    print('part1:', ans1)

    nums = nums + list(range(10, 1000001))
    ans2 = part2(nums, 10000000)
    print('part2:', ans2)


main()
