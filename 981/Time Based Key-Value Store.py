from collections import defaultdict
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictstore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictstore[key].append((timestamp,value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        valuelist = self.dictstore[key]
        l = 0
        r = len(valuelist)
        while l < r:
            m = l+(r-l)//2
            if valuelist[m][0]>timestamp:
                r = m
            else:
                l = m+1
        return "" if l == 0 else valuelist[l-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)