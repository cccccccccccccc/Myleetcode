"""
LRU discards the least recently used cache. we need to impelement the fuction put and get in O(1) time complexity. so we need find element in O(1) which means doulbe linked list is
useful .
initialize list node  have value key and two pointer for prev and next
initialize LRUCache class  init head and end linked list length of list curnum and a dict to help find value immediately
construct  function inserthead and removenode 
when we call get we need to do some thing : check if there are key in cache  not return -1  yes remove it from current position and insert to the head 
when we call put we need to do sth: check if the capacity is full if not check if the element is in dict if yes do what get do  if no put it in dict add num and put it to head
                                    if capacity is full remove last node from end and do the same as a new node insert do.
"""
from collections import defaultdict

"""
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

"""
class LinkNode:
    def __init__(self,key = 0,value = 0,prev = None,next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkNode()
        self.end = LinkNode()
        self.head.next = self.end
        self.end.prev = self.head
        self.length = capacity
        self.num = 0
        self.dict = defaultdict(int)
    def inserthead(self,node):
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next.prev = node
    def removenode(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        value = node.value
        self.removenode(node)
        self.inserthead(node)
        return value
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.inserthead(node)           
        else:
            if self.num == self.length:
                del self.dict[self.end.prev.key]
                self.removenode(self.end.prev)
            else:
                self.num+=1
            newnode = LinkNode(key,value)
            self.dict[key]=newnode
            self.inserthead(newnode)
        return

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