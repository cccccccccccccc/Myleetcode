class ListNode:
    def __init__(self, key=0,val=0,prev= None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0)
        self.end = ListNode(0)
        self.head.next = self.end
        self.end.prev = self.head
        self.length = capacity
        self.num = 0
        self.dict = {}
    def inserthead(self,node):
        node.next = self.head.next
        node.prev = self.head
        node.prev.next = node
        node.next.prev = node
        return    
    def removenode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        value = node.val
        self.removenode(node)
        self.inserthead(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.removenode(node)
            self.inserthead(node)        
        else:
            newnode = ListNode(key,value)
            self.dict[key] = newnode
            if self.num == self.length:
                del self.dict[self.end.prev.key]
                self.removenode(self.end.prev)
                self.num-=1
            self.inserthead(newnode)
            self.num+=1
            return
# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]            
A = LRUCache(2) 
A.put(1,1)
A.put(2,2)
print(A.get(1))
A.put(3,3)
print(A.get(2))
A.put(4,4)
print(A.get(1))
print(A.get(3))
print(A.get(4))
