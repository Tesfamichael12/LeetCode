# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        l = dummy
        r = dummy
        for _ in range(right):
            r = r.next
        for _ in range(left - 1):
            l = l.next
        
        last = l
        l = l.next
        last.next = r
        prev = r.next

        for _ in range(right - left + 1):
            nxt = l.next
            l.next = prev
            prev = l
            l = nxt
        
        return dummy.next