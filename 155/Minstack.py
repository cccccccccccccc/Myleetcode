"""
timecomplexity = O(1) spacecomlexity = O(n)
use tuple as the element of the stacklist,each tuple contain item X and cur min item.
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stacklist = []
        

    def push(self, x: int) -> None:
        if len(self.stacklist) == 0:
            self.stacklist.append((x,x))
        else:
            m = self.getMin()
            self.stacklist.append((x,min(x,m)))

    def pop(self) -> None:
        self.stacklist.pop()

    def top(self) -> int:
        return self.stacklist[-1][0]

    def getMin(self) -> int:
        return self.stacklist[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()