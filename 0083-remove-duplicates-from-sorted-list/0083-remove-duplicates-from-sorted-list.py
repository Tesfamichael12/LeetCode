# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = head, head
        while r:
            while r and l.val == r.val:
                r = r.next
            l.next = r
            l = r
        return head