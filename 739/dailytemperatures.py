from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if T is None:
            return T
        output = [0]*len(T)
        stk = []
        for i in range(len(T)):
            if stk:
                while stk:
                    tmptemper = stk[-1][0]
                    tmpidx = stk[-1][1]
                    if T[i]>tmptemper:
                        output[tmpidx] = i - tmpidx
                        stk.pop()
                    else:
                        break
            stk.append([T[i],i])
        return output
A = Solution()
a = [73,74,75,71,69,72,76,73]
b = [30,30]
print(A.dailyTemperatures(a))
print(A.dailyTemperatures(b))