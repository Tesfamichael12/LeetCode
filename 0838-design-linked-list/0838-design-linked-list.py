class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def display(self, ll : ListNode):
        res = []
        temp = ll
        while temp :
            res.append(temp.val)
            print(temp.val)
            temp = temp.next
        
        return res
    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp.val 

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        newnode = ListNode(val)
        temp = self.head
        if index <= 0:
            newnode.next = temp
            self.head = newnode
        else:
            for _ in range(index - 1):
                temp = temp.next
            newnode.next = temp.next
            temp.next = newnode
        
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        temp = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                if temp == None:
                    return

                temp = temp.next
            
            temp.next = temp.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)