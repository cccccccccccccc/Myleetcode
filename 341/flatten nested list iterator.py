# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
    #     self.getall(nestedList)
    # def getall(self,nestedList):
    #     if nestedList == None:
    #         return
    #     for i in nestedList:
    #         if i.isInteger() == True:
    #             print(i.getInteger())
    #         else:
    #             self.getall(i.getList())
    #     return
        self.nextint = 0
        if nestedList == None:
            self.stack = []
        else:
            self.stack = [(nestedList,-1)]
        
    def next(self) -> int:
        return self.nextint
    
    def hasNext(self) -> bool:
        while len(self.stack) > 0:
            curtuple = self.stack.pop()
            curlist = curtuple[0]
            index = curtuple[1]
            if index+1 < len(curlist):
                if curlist[index+1].isInteger() == True:
                    self.nextint = curlist[index+1].getInteger()
                    self.stack.append((curlist,index+1))
                    return True
                else:
                    self.stack.append((curlist,index+1))
                    nextlist = curlist[index+1].getList()
                    self.stack.append((nextlist,-1))
                    continue
        return False
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
            
    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False

"""
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
