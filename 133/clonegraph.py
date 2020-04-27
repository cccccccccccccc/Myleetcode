"""
# Definition for a Node.
"""
from collections import deque
from typing import List
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def clonenode(self, oldnode,nodedict):
        newnode = Node()
        newnode.val = oldnode.val
        newnode.neighbors = []
        nodedict[oldnode] = newnode
        return newnode
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        if len(node.neighbors) == 0:
            tmp = Node()
            tmp.val = node.val
            tmp.neighbors = []
            return tmp
        nodedeque = deque()
        nodedict = {}
        nodedeque.append(node)
        self.clonenode(node,nodedict)
        while len(nodedeque) != 0:
            oldnode = nodedeque.popleft()
            newnode = nodedict[oldnode]
            for tmpoldnode in oldnode.neighbors:
                if tmpoldnode not in nodedict:
                    tmpnewnode = self.clonenode(tmpoldnode,nodedict)
                    nodedeque.append(tmpoldnode)
                else:
                    tmpnewnode = nodedict[tmpoldnode]
                newnode.neighbors.append(tmpnewnode)  
        return nodedict[node]
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        nodedeque = deque()
        nodedict = {}
        nodedeque.append(node)
        clonenode = Node(node.val)
        nodedict[node] = clonenode
        while len(nodedeque) != 0:
            oldnode = nodedeque.popleft()
            clonenode = nodedict[oldnode]
            for tmpoldnode in oldnode.neighbors:
                if tmpoldnode not in nodedict:
                    tmpclonenode = Node(tmpoldnode.val)
                    nodedict[tmpoldnode] = tmpclonenode
                    nodedeque.append(tmpoldnode)
                else:
                    tmpclonenode = nodedict[tmpoldnode]
                clonenode.neighbors.append(tmpclonenode)  
        return nodedict[node]

A = Solution()
a = Node()
b = Node()
c = Node()
d = Node()
a.val = 1
a.neighbors = [b,d]
b.val = 2
b.neighbors = [a,c]
c.val = 3
c.neighbors = [b,d]
d.val = 4
d.neighbors = [a,c]
print(A.cloneGraph(a))