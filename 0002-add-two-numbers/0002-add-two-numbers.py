# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse both the linked lists
        # def reverseLL(head):
        #     cur = head
        #     prev = None
        #     while cur:
        #         nxt = cur.next
        #         cur.next = prev
        #         prev = cur
        #         cur = nxt
            
        #     return prev
        
        # l1 = reverseLL(l1)
        # l2 = reverseLL(l2)

        carry = 0
        val = 0
        res = ListNode(None)
        ans = res
        while l1 and l2:
            val = l1.val + l2.val + carry
            q, carry = val % 10, val // 10

            newnode = ListNode(q)
            res.next = newnode
            res = res.next

            l1 = l1.next
            l2 = l2.next
        
        # adding the remaining digits
        while l1:
            val = l1.val + carry
            q, carry = val % 10, val // 10

            newnode = ListNode(q)
            res.next = newnode
            res = res.next

            l1 = l1.next
        
        while l2:
            val = l2.val + carry
            q, carry = val % 10, val // 10

            newnode = ListNode(q)
            res.next = newnode
            res = res.next

            l2 = l2.next
        
        if carry > 0:
            newnode = ListNode(carry)
            res.next = newnode
        
        return ans.next
