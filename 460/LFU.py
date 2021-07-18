from collections import defaultdict

class LFUNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.frequency = 0
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self. minfrequency = 0
        self.keynodedict = defaultdict(list)
        self.freqnodedict = defaultdict(list)

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)