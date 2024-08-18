# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv, cur = None, head
        while cur:
            next_temp = cur.next
            cur.next = prv
            prv = cur
            cur = next_temp

        return prv