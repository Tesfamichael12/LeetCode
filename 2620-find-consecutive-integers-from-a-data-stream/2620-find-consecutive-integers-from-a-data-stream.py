class DataStream:

    def __init__(self, value: int, k: int):
        self.q = deque()
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        # print(self.q)
        if num != self.value:
            self.q = deque()
            return False
        else:
            self.q.append(num)
        
        if len(self.q) >= self.k:
            if len(self.q) > self.k: 
                self.q.popleft()
            
            return True
        else:
            return False
        
 

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)