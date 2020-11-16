from typing import List
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                res = res*10 + int(s[i])
            if s[i] in "+-*/"or i == len(s)-1:
                if sign == "+":
                    stack.append(res)
                if sign == "-":
                    stack.append(-res)
                if sign == "*":
                    stack.append(stack.pop()*res)
                if sign == "/":
                    stack.append(int(stack.pop()/res))
                res = 0
                sign = s[i]
        return sum(stack)

A = Solution()
s = "10 + 11*11 - 10"
s = "10000*2"
s = "14-3/2"
print(A.calculate(s))