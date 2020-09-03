class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.insert(0,x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        result = self.queue[-1]
        self.queue.remove(self.queue[-1])
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if len(self.queue) ==0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()