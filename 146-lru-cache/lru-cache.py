class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lrucache = {}

    def get(self, key: int) -> int:
        if key not in self.lrucache: 
            return -1
        self.lrucache[key] = self.lrucache.pop(key)
        return self.lrucache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.lrucache:
            self.lrucache.pop(key)
        self.lrucache[key] = value
        if len(self.lrucache) > self.capacity:
            self.lrucache.pop(next(iter(self.lrucache)))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)