# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        valu_one = []
        valu_two = []
        while l1 or l2:
            valu_one.append(l1.val if l1 else 0)
            valu_two.append(l2.val if l2 else 0)
        num_one = list(reversed(valu_one))
        num_two = list(reversed(valu_two))
        _sum = int("".join(map(str, num_one))) + int("".join(map(str, num_two)))
        result = list(reversed(list(map(int, str(_sum)))))
        return result

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _head = ListNode(0)
        head = _head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, value = divmod(val1 + val2 + carry, 10)
            head.next = ListNode(value)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return _head.next

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
l1 = create_linked_list(l1)
l2 = create_linked_list(l2)
result = Solution()
result = result.addTwoNumbers(l1, l2)
print_linked_list(result)


