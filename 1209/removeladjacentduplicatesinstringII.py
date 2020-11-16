from typing import List
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[]
        for ch in s:
            if len(stack) != 0 and stack[-1][0] == ch:
                tmp = stack.pop()
                if tmp[1]+1 != k:
                    stack.append([tmp[0],tmp[-1]+1]) 
            else:
                stack.append([ch,1])
        res=""
        while len(stack)!=0:
            tmp = stack.pop()
            for i in range(tmp[1]):
                res=tmp[0]+res
        return res
A = Solution()
s = "deeedbbcccbdaa"
k = 3
print(A.removeDuplicates(s,k))
