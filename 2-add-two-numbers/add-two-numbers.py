# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:

        if not l1 and not l2 and carry == 0: return None  

        vl1 = l1.val if l1 else 0
        vl2 = l2.val if l2 else 0

        total = vl1 + vl2 + carry
        carry = total // 10
        new_val = total % 10

        curr_node = ListNode(new_val)

        new_l1 = l1.next if l1 else None
        new_l2 = l2.next if l2 else None
        curr_node.next = self.addTwoNumbers(new_l1, new_l2, carry)

        return curr_node