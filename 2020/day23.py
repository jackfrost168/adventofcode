# with open('test.txt', 'r') as f:
# with open('input/input23.txt', 'r') as f:
#     f = f.readlines()


def part(nums, moves):
    m = 0
    while m < moves:
        current = nums[0]
        first, second, third = nums[1:4]
        nums.pop(1)
        nums.pop(1)
        nums.pop(1)
        des_cup = current - 1
        if des_cup == 0:
            des_cup = 9
        while des_cup not in nums:
            des_cup = des_cup - 1
            if des_cup == 0:
                des_cup = 9
        des_index = nums.index(des_cup)
        nums.insert(des_index + 1, first)
        nums.insert(des_index + 2, second)
        nums.insert(des_index + 3, third)

        nums = nums[1:] + nums[0:1]
        m = m + 1

    index_1 = nums.index(1)
    ans = nums[index_1+1:] + nums[0: index_1]
    ans = [str(s) for s in ans]
    print('part1:', ''.join(ans))


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def part2(nums):
    nodes = [Node(value) for value in nums]
    for i in range(len(nodes)):
        if i == 0:
            nodes[i].prev = nodes[-1]
            nodes[i].next = nodes[i+1]
        elif i == len(nodes) - 1:
            nodes[i].next = nodes[0]
            nodes[i].prev = nodes[i-1]
        else:
            nodes[i].next = nodes[i+1]
            nodes[i].prev = nodes[i-1]

    value_pos = {}
    for i, value in enumerate(nums):
        value_pos[value] = i

    current = nodes[0]
    m = 0
    while m < 10000000:
        # if m % 1000000 == 0:
        #     print(m)
        first = current.next
        second = current.next.next
        third = current.next.next.next

        des_cup = current.value - 1
        if des_cup == 0:
            des_cup = 1000000
        while des_cup not in range(1, 1000001) or (des_cup == first.value or
                                                   des_cup == second.value or
                                                   des_cup == third.value):
            des_cup = des_cup - 1
            if des_cup == 0:
                des_cup = 1000000
        des_index = value_pos[des_cup]

        tmp = current.next
        current.next = third.next
        third.next.prev = current

        third.next = nodes[des_index].next
        nodes[des_index].next.prev = third
        nodes[des_index].next = first
        first.prev = nodes[des_index]

        current = current.next
        m = m + 1

    id_1 = value_pos[1]
    #print(nodes[id_1].next.value, nodes[id_1].next.next.value)
    print('part2:', nodes[id_1].next.value*nodes[id_1].next.next.value)


def main():
    f = '942387615'
    nums = list(f)
    nums = [int(s) for s in f]
    part(nums, 100)

    f = '942387615'

    nums = list(f)
    nums = [int(s) for s in f]
    nums = nums + list(range(10, 1000001))
    part2(nums)


main()




