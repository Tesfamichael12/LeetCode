# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prv = None
        cur = mid
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        
        end = prv
        start = head
        # print(end.val)

        res = start.val + end.val
        while start != mid:
            res = max(res, start.val + end.val)
            start = start.next
            end = end.next
        
        return res