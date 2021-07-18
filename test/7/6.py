from typing import List
from collections import defaultdict
import heapq
class LinkNode:
    def __init__(self,x = 0,next= None):
        self.value = x
        self.next = next
class Solution:
    def MergeKlinklist(self,ListKlink:List):
        heapKLL = []
        heapq.heapify(heapKLL)
        indexlist = [None]*len(ListKlink)
        for i in range(len(ListKlink)):
            tmp = (ListKlink[i].value,i)
            indexlist[i]=ListKlink[i]
            heapq.heappush(heapKLL,tmp)
        ansHead = LinkNode(0)
        curnode = ansHead
        while len(heapKLL)>0:
            tmpindex = heapq.heappop(heapKLL)[1]
            tmpnode = indexlist[tmpindex]
            curnode.next = tmpnode
            curnode = curnode.next
            nextheapnode = tmpnode.next
            if nextheapnode is not None:
                indexlist[tmpindex] = nextheapnode
                heapq.heappush(heapKLL,(nextheapnode.value,tmpindex))
        return ansHead.next

A = Solution()
b = LinkNode(1)
b1 = LinkNode(2)
b2 = LinkNode(4)
b.next = b1
b1.next = b2
c = LinkNode(3)
c1 = LinkNode(3)
c2 = LinkNode(5)
c.next = c1
c1.next = c2
d = LinkNode(2)
d1 = LinkNode(4)
d2 = LinkNode(7)
d.next = d1
d1.next = d2
a = [b,c,d]
e = []
print(A.MergeKlinklist(e))