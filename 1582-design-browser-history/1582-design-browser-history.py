# class for a doubly linked list
class ListNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prv = None

class BrowserHistory:

    def __init__(self, homepage: str):
        # add start and end node for efficent traversal and adding new nodes
        self.start = ListNode(None)
        self.end = ListNode(None)

        self.history = ListNode(homepage) # add the home page to the first node

        # link up the the start and end with the homepage node
        self.start.next, self.history.prv = self.history, self.start
        self.end.prv, self.history.next = self.history, self.end

        self.cur = self.history# to save the current page location

    def visit(self, url: str) -> None:
        # add at the current page location of the history linked list using the end node
        newnode = ListNode(url)
        self.cur.next, newnode.prv = newnode, self.cur
        self.end.prv, newnode.next = newnode, self.end

        self.cur = newnode
        

    def back(self, steps: int) -> str:
        temp = self.cur
        while steps > 0 and temp.prv.prv:
            temp = temp.prv
            steps -= 1

        self.cur = temp
        return temp.url

    def forward(self, steps: int) -> str:
        temp = self.cur
        while steps > 0 and temp.next.next:
            temp = temp.next
            steps -= 1
        self.cur = temp
        return temp.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)