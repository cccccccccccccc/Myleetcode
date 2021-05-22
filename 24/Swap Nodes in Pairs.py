# Definition for singly-linked list.
"""
timecomplexity = O(n) spacecomplexity = O(1)
We iterate the linked list with jumps in steps of two
swap the pairs of node as we go, before we jump to the next pair represent the two nodes to be swapped by firstnode and secondnode
swap the two nodes 
We aslo need to assign prevnode'next to the head of swapped pair this step would ensure the currently swapped pair is linked correctly to the end of previously swapped list.
This is an iterative step, so the nodes are swapped on the go and attached to the previously swapped list. And in the end we get the final swapped list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        newhead = ListNode()
        newhead.next = head
        prev_node = newhead
        while head and head.next:
            firstnode = head
            secondnode = head.next
            prev_node.next = secondnode
            firstnode.next = secondnode.next
            secondnode.next = firstnode
            prev_node = firstnode
            head = firstnode.next
        return newhead.next