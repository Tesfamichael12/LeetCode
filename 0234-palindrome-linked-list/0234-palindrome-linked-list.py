# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        # reverse the second half

        prev = None
        cur = mid
        nxt = cur
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        end = prev
        start = head

        while start and end:
            if start.val != end.val:
                return False
            
            start = start.next
            end = end.next
        
        return True