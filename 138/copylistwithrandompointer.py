#timecomplexity O(n) spacecomplexity O(n)
'''
use a dictornary to remember node between original list to copy node 
iterate the original list: if the copy node is already in nodedict get it ,or create a new one and put into nodedict
remember to use the next of the node as the current node to be operated. 

another way is using recursive to copy node
a global dict remind the relation between orig and copy node
if head is none:
    return none
find node from dict or create
recursive call function to get node.next and node.random
return node
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        markdict = {}
        dew = Node(0)
        cur = dew
        while head is not None:
            if head not in markdict.keys():
                cur.next = Node(head.val)
                markdict[head] = cur.next
            else:
                cur.next = markdict[head]          
            if head.random is not None:
                tmprandom = head.random
                if tmprandom in markdict.keys():
                    cur.next.random = markdict[tmprandom]
                else:
                    cur.next.random = Node(tmprandom.val)
                    markdict[tmprandom] = cur.next.random
            else:
                cur.next.random = None
            cur = cur.next
            head = head.next
        return dew.next

A = Solution()
a = Node(7)
b = Node(13)
c = Node(11)
d = Node(10)
e = Node(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None
a.random = None
b.random = a
c.random = e
d.random = c
e.random = a
print (A.copyRandomList(a))