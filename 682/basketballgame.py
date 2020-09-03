from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if len(ops) == 0:
            return  0
        roundpointstack = []
        roundsum = 0
        for i in ops:
            if i == "D" :
                roundpointstack.append(roundpointstack[-1]*2)
                roundsum+=roundpointstack[-1]
            elif i == "C" :
                roundsum-=roundpointstack[-1]
                roundpointstack.pop()
            elif i == "+":
                roundpointstack.append(roundpointstack[-1]+roundpointstack[-2])
                roundsum+=roundpointstack[-1]
            else:
                roundpointstack.append(int(i))
                roundsum+=roundpointstack[-1]
        return roundsum
A = Solution()
a = ["-5","2","C","D","+"]
print(A.calPoints(a))