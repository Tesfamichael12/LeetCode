# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # see the constraints [0, 300]-> number of nodes
        if not head or not head.next: 
            return head

        prv = head
        cur = head.next
        while cur:
            if prv.val == cur.val:
                prv.next = cur.next
            else:
                prv = cur

            cur = cur.next
        
        return head