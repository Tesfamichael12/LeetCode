# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def delete(node):
            if not node: 
                return None
            
            node.next = delete(node.next)
            if node.val != val:
                return node
            else:
                return node.next
        
        return delete(head)