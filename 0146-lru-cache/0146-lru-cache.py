
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        
        self.cache[key] = value
        
        if len(self.cache) > self.cap:
            self.cache.pop(next(iter(self.cache)))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)