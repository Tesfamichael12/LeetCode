# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            vl1 = l1.val if l1 else 0
            vl2 = l2.val if l2 else 0

            total = vl1 + vl2 + carry
            carry = total // 10
            new_val = total % 10

            tail.next = ListNode(new_val)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next