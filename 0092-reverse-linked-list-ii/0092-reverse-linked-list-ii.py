# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        cur = dummy.next
        
        # find the position
        for i in range(1,m):
            cur = cur.next
            pre = pre.next 
        
        # reverse
        for i in range(n-m):
            temp = cur.next
            cur.next = temp.next
            temp.next  = pre.next
            pre.next = temp
        
        return dummy.next