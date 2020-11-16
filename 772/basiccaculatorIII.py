'''
If char is a digit, we continue construct number with it.
If char is (, we need to push the op in stack, and reset op to +
If char is one of +, -, *, /, ), we have reached end of an partial expression. so we evaluate the result of the partial expression. If the char is ), we have to pop all the items out until we reach the last op before (, and then evaluate the partial expression. We then set op as current char.
Finally, after we reach the end of the string, we do another evaluation of the expression to include the last num.
'''
from typing import List
class Solution:
    def calculate(self, s: str) -> int:
        def update(sign,num):
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(int(stack.pop()*num))
            elif sign == "/":
                stack.append(int(stack.pop()/num))
        stack = []
        num = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in "+-*/)":
                update(sign,num)
                if s[i] == ")":
                    num = 0
                    while isinstance(stack[-1],int):
                        num +=stack.pop()
                    sign = stack.pop()
                    update(sign,num)
                sign,num = s[i],0
            elif s[i] == "(":
                stack.append(sign)
                num = 0
                sign = "+"
        update(sign,num)
        return sum(stack)
A = Solution()
s = "2*(5+5*2)/3+(6/2+8)"
print(A.calculate(s))