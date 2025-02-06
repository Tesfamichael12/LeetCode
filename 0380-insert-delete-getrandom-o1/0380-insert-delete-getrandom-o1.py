class RandomizedSet:

    def __init__(self):
        self.hashset = set()

    def insert(self, val: int) -> bool:
        if val in self.hashset:
            return False
        else:
            self.hashset.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.hashset:
            self.hashset.remove(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        return random.choice(list(self.hashset))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()