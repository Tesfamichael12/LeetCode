# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(None)
        # dummy.next = head
        if not head:
            return head

        odd = head
        even = head.next
        s = even

        while even and even.next and odd and odd.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = s
        return head