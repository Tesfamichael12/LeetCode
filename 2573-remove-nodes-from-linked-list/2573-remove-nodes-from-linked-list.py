# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def stack(node, mx):
            if not node:
                return None, mx
            
            node.next, mx = stack(node.next, mx)
            print( mx.val, node.val)
            if mx.val <= node.val:
                return node, node
            else:
                return mx, mx

        new_head, _ = stack(head, ListNode())
        return new_head