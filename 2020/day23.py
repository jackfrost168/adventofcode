# with open('test.txt', 'r') as f:
# with open('input/input23.txt', 'r') as f:
#     f = f.readlines()
# f = '942387615'
# #f = '389125467'
# nums = list(f)
# nums = [int(s) for s in f]
#
# def part(nums, moves):
#     m = 0
#     while m < moves:
#         current = nums[0]
#         first, second, third = nums[1:4]
#         nums.pop(1)
#         nums.pop(1)
#         nums.pop(1)
#         des_cup = current - 1
#         if des_cup == 0:
#             des_cup = 9
#         while des_cup not in nums:
#             des_cup = des_cup - 1
#             if des_cup == 0:
#                 des_cup = 9
#         des_index = nums.index(des_cup)
#         nums.insert(des_index + 1, first)
#         nums.insert(des_index + 2, second)
#         nums.insert(des_index + 3, third)
#
#         print('moves:', m)
#         print(nums)
#
#         nums = nums[1:] + nums[0:1]
#
#         m = m + 1
#     print(nums)
#     index_1 = nums.index(1)
#     ans = nums[index_1+1:] + nums[0: index_1]
#     print(ans)
# part(nums, 10000)



# f = '942387615'
# #f = '389125467'
# nums = list(f)
# nums = [int(s) for s in f]
# #nums = nums + list(range(10, 1000001))
#
# class Node(object):
#     """双向链表节点"""
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# class DLinkList(object):
#     """双向链表"""
#     def __init__(self):
#         self._head = Node(-1)
#         self._head.next = _head
#         self._head.prev
#
#     def is_empty(self):
#         """判断链表是否为空"""
#         return self._head.next == None
#
#     # def length(self):
#     #     """返回链表的长度"""
#     #     cur = self._head
#     #     count = 0
#     #     while cur != None:
#     #         count += 1
#     #         cur = cur.next
#     #     return count
#     #
#     # def travel(self):
#     #     """遍历链表"""
#     #     cur = self._head
#     #     while cur != None:
#     #         print cur.item,
#     #         cur = cur.next
#     #     print ""
#
#     def add(self, item):
#         """头部插入元素"""
#         node = Node(item)
#         if self.is_empty():
#             # 如果是空链表，将_head指向node
#             self._head = node
#         else:
#             # 将node的next指向_head的头节点
#             node.next = self._head
#             # 将_head的头节点的prev指向node
#             self._head.prev = node
#             # 将_head 指向node
#             self._head = node
#
#     def append(self, item):
#         """尾部插入元素"""
#         node = Node(item)
#         if self.is_empty():
#             # 如果是空链表，将_head指向node
#             self._head = node
#         else:
#             # 移动到链表尾部
#             cur = self._head
#             while cur.next != None:
#                 cur = cur.next
#             # 将尾节点cur的next指向node
#             cur.next = node
#             # 将node的prev指向cur
#             node.prev = cur
#
#
#
#     def search(self, item):
#         """查找元素是否存在"""
#         cur = self._head
#         while cur != None:
#             if cur.item == item:
#                 return True
#             cur = cur.next
#         return False
#
#     def append_node(self, cur, item):
#         node = Node(item)
#         while cur.next != None:
#             cur = cur.next
#         # 将尾节点cur的next指向node
#         cur.next = node
#         # 将node的prev指向cur
#         node.prev = cur
#
#     def insert(self, pos, item):
#         """在指定位置添加节点"""
#         if pos <= 0:
#             self.add(item)
#         elif pos > (self.length()-1):
#             self.append(item)
#         else:
#             node = Node(item)
#             cur = self._head
#             count = 0
#             # 移动到指定位置的前一个位置
#             while count < (pos-1):
#                 count += 1
#                 cur = cur.next
#             # 将node的prev指向cur
#             node.prev = cur
#             # 将node的next指向cur的下一个节点
#             node.next = cur.next
#             # 将cur的下一个节点的prev指向node
#             cur.next.prev = node
#             # 将cur的next指向node
#             cur.next = node
#
#     def remove(self, item):
#         """删除元素"""
#         if self.is_empty():
#             return
#         else:
#             cur = self._head
#             if cur.item == item:
#                 # 如果首节点的元素即是要删除的元素
#                 if cur.next == None:
#                     # 如果链表只有这一个节点
#                     self._head = None
#                 else:
#                     # 将第二个节点的prev设置为None
#                     cur.next.prev = None
#                     # 将_head指向第二个节点
#                     self._head = cur.next
#                 return
#             while cur != None:
#                 if cur.item == item:
#                     # 将cur的前一个节点的next指向cur的后一个节点
#                     cur.prev.next = cur.next
#                     # 将cur的后一个节点的prev指向cur的前一个节点
#                     cur.next.prev = cur.prev
#                     break
#                 cur = cur.next
#
# cups = DLinkList()
# tmp = cups._head
# for num in nums:
#     tmp.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

f = '942387615'
#f = '389125467'
nums = list(f)
nums = [int(s) for s in f]
nums = nums + list(range(10, 1000001))
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
    if m % 10000 == 0:
        print(m)
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
print(nodes[id_1].next.value, nodes[id_1].next.next.value)
print(nodes[id_1].next.value*nodes[id_1].next.next.value)






