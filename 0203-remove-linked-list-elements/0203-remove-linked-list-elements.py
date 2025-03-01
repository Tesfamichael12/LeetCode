# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(None)
        dummy.next = head
        temp = dummy
        prev = temp

        while temp.next:
            prev = temp
            temp = temp.next

            if temp.val == val:
                prev.next = temp.next
                temp = prev
        

        return dummy.next