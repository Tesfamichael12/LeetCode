class ProductOfNumbers:

    def __init__(self):
        self.prifix = [1]


    def add(self, num: int) -> None:
        if num!= 0:
            self.prifix.append(self.prifix[-1] * num)
        else:
            self.prifix = [1]        

    def getProduct(self, k: int) -> int:
        if k >= len(self.prifix):
            return 0
        else:
            return self.prifix[-1] // self.prifix[-k-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)