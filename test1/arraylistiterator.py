from typing import List
from collections import deque
class Iterator:
    def __init__(self,input):
        self.totalarray = input
        self.nextelement = [0,0]
        self.ishas_next = False
        return
    def has_next(self):
        self.ishas_next = True
        if self.nextelement[1]+1 < len(self.totalarray[self.nextelement[0]]):
            self.nextelement = [self.nextelement[0],self.nextelement[1]+1]
            return True
        i = 1
        while self.nextelement[0]+i < len(self.totalarray):
            if len(self.totalarray[self.nextelement[0]+i])<=0:
                i+=1
                continue
            else:
                self.nextelement = [self.nextelement[0]+i,0]
                return True
        return False
    def next(self):
        if self.ishas_next == False:
            self.has_next()   
        answer = self.totalarray[self.nextelement[0]][self.nextelement[1]]
        self.ishas_next = False
        return answer
    def remove(self): 
        self.totalarray[self.nextelement[0]].pop(self.nextelement[1])
        return
input = [[],[1,2,3],[],[4],[5]]
A = Iterator(input)
while (A.has_next()):
    if (A.next()%2) == 0:
        A.remove()
A = Iterator(input)
while(A.has_next()):
    print(A.next())

