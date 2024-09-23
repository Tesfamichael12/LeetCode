class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUCache = {}

    def get(self, key: int) -> int:
        if key not in self.LRUCache:
            return -1
        self.LRUCache[key] = self.LRUCache.pop(key)
        return self.LRUCache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache: 
            self.LRUCache.pop(key)
        self.LRUCache[key] = value
        if len(self.LRUCache) > self.capacity:
            self.LRUCache.pop(next(iter(self.LRUCache)))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)