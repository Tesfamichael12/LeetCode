# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        def recursion(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node or not node.next:
                return node
            
            lastNode = node
            prevNode = None
            
            while lastNode.next:
                prevNode = lastNode
                lastNode = lastNode.next
            
            prevNode.next = None

            remainingPart = node.next
            
            lastNode.next = recursion(remainingPart)
            
            node.next = lastNode

            return node

        recursion(head)