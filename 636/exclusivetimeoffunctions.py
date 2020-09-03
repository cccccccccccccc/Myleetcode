from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        timespend = [0]*n
        idstack = []
        usedtime = 0
        for s in logs:
            slist = s.split(':')
            if idstack and int(slist[0]) == idstack[-1][0] and slist[1]!= idstack[-1][3]:
                timespend[int(slist[0])] += int(slist[2])-idstack[-1][1]-idstack[-1][2]+1
                
                usedtime = int(slist[2])-idstack[-1][1]+1                
                idstack.pop()
                if idstack:
                    idstack[-1][2] += usedtime
            else:
                usedtime = 0
                idstack.append([int(slist[0]),int(slist[2]),0,slist[1]])

        return timespend

A = Solution()
a = 3
b = ["0:start:0","1:start:2","2:start:3","/2:end:4","1:end:5","0:end:6"]
c = 1
d = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(A.exclusiveTime(c,d))