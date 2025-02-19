# Definition for singly-linked list.
# class ListNode:
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        temp = dummy
        l = temp
        r = temp
        while n > 0:
            r = r.next
            n -= 1

        while r and r.next:
            r = r.next
            l = l.next
        
        l.next = l.next.next

        return dummy.next
