# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = ListNode(None)
        l_temp = l
        r = ListNode(None)
        r_temp = r

        temp = head
        while temp:
            if temp.val < x:
                l.next = ListNode(temp.val)
                l = l.next
            else:
                r.next = ListNode(temp.val)
                r = r.next

            temp = temp.next
        
        r.next = None
        
        l.next = r_temp.next
    
        return l_temp.next