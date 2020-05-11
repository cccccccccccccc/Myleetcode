from typing import List
class Node:
    def __init__(self,id = 0):
        self.id = id
        self.dfn = 0
        self.low = 0
        self.neighbers = []
class Solution:
    def getcomponent(self, node: Node,newdfn,newlow,parent):
        if node.dfn != 0:
            return node.low
        node.dfn = newdfn
        node.low = newlow
        for child in node.neighbers: 
            if child != parent:
                tmplow = self.getcomponent(child,newdfn+1,newlow+1,node)
                if tmplow < node.low:
                    node.low = tmplow
        return node.low       
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if n <= 1:
            return connections
        graphdict = {}
        returnlist = []
        for edge in connections:
            id  = edge[0]
            neighbersid = edge[1]
            if id in graphdict:
                node = graphdict[id]
            else:
                node = Node(id)
                graphdict[id] = node
            if neighbersid in graphdict:
                neighbersnode = graphdict[neighbersid]
            else:
                neighbersnode = Node(neighbersid)
                graphdict[neighbersid] = neighbersnode
            node.neighbers.append(neighbersnode)
            neighbersnode.neighbers.append(node)
        self.getcomponent(node,1,1, None)
        for edge in connections:
            node1 = graphdict[edge[0]]
            node2 = graphdict[edge[1]]
            if node1.dfn > node2.dfn:
                node1,node2 = node2,node1
            if node1.dfn < node2.low:
                returnlist.append(edge)
        return returnlist
A = Solution()
a=4
b = [[0,1],[1,2],[2,0],[1,3]]
print(A.criticalConnections(a,b))