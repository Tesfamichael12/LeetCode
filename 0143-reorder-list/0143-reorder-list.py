# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middel of the linked list 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half part
        prv = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prv
            prv = cur
            cur = temp

        # Now let's merge the two halfs alternatively
        first, second = head, prv
        while second.next:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2