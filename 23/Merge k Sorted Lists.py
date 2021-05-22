# Definition for singly-linked list.
"""
timecomplexity = O(nlogk) spacecomplexity = O(k)
use heap to get min val in each listnode
first put a tuple each list's first node's val and index in list into heap
then iterate heap pop min val get index from lists if node.next is not Null use index to find the next node to put into the heap
every time after push the node in heap shift list[index] to list[index].next
"""
from typing import List
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        cur = head
        minnodeheapq =[]
        heapq.heapify(minnodeheapq)
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(minnodeheapq,(l.val,i))
        while len(minnodeheapq)!= 0:
            index = heapq.heappop(minnodeheapq)[1]
            tmp = lists[index]
            cur.next = tmp
            cur = cur.next
            if tmp.next:
                heapq.heappush(minnodeheapq,(tmp.next.val,index))
                lists[index] = lists[index].next
        return head.next

A = Solution()
a = ListNode(1)
b = ListNode(2)
c  = ListNode(1)
d = ListNode(3)
a.next = b
c.next = d
lists = [a,c]
print(A.mergeKLists(lists))