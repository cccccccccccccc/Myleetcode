"""
timecomplexity = O(n) spacecomlexity = O(n)
every parenthese is belong to a couple () [] {}
so we can use dict to solve this problem
construct a dict key is left parenthese value is right (or key is right parenthese)
iterate the string 
if current char is left parenthese put into the stack
else check if stack isnot empty and pop the last one in stack to check if they are couple 
if not return false 
make sure stack has no char in the end or the string is not True
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) ==0:
            return True
        if len(s) ==1:
            return False
        if len(s)%2 != 0:
            return False
        stacklist = []
        dictparentheses = {'(':')','[':']','{':'}'}
        if s[0] in dictparentheses.keys():
            stacklist.append(s[0])
        else:
            return False
        for i in s[1:]:
            if i in dictparentheses.keys():
                stacklist.append(i)
            elif len(stacklist) != 0:
                if dictparentheses[stacklist.pop()] != i:
                    return False
            else:
                return False
        if len(stacklist) != 0:
            return False
        return True
"""
"()"
""
"("
")"
"((()))"
"()()(){}[]"
"({)}"
"()()((())"
"""
A = Solution()
a = "()))"
print(A.isValid(a))