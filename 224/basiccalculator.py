from typing import List
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        operand = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                operand = operand*10 + int(ch)
            elif ch == "+":
                res+=sign * operand
                sign = 1
                operand = 0
            elif ch == "-":
                res+= sign* operand
                sign = -1
                operand = 0
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ")":
                res +=sign*operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res+sign*operand
A = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
c = "((((((1+2))))))"
d = "1-(2)+1-30"
print(A.calculate(d))


"""
class Solution:
    def getsubcal(self,i):
        tmp = self.rem.pop()
        tmpresult = self.result.pop()
        if tmp == "+":
            tmpresult+=int(i)
        else:
            tmpresult-=int(i)
        self.result.append(tmpresult)
        self.rem.pop()
        self.rem.append(str(tmpresult))

    def calculate(self, s: str) -> int:
        self.rem = []
        self.result = []
        for i in s:
            if i == " ":
                continue
            if i == "(":
                if len(self.rem) == 0:
                    continue
                else:
                    self.rem.append(i)
            elif i == "+" or i == "-":
                self.rem.append(i)
            elif i == ")":
                if len(self.rem) == 1:
                    continue
                tmp = self.rem.pop()
                self.result.pop()
                self.rem.pop()
                self.getsubcal(tmp)
            else:
                if len(self.rem) == 0:
                    self.rem.append(i)
                    self.result.append(int(i))
                else:
                    if self.rem[-1] == "(":
                        self.rem.append(i)
                        self.result.append(int(i))
                    else:
                        self.getsubcal(i)

        return self.result[-1]
A = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
c = "((((((1+2))))))"
d = "1-(2)+1-3"
print(A.calculate(d))
"""
            