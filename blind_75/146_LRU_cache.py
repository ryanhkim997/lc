from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.vals = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.vals:
            self.vals.move_to_end(key)
            return self.vals[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.vals:
            self.vals[key] = value
            self.vals.move_to_end(key)
        else:
            if len(self.vals) == self.capacity:
                self.vals.popitem(last=False)
            self.vals[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)