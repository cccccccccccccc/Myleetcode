from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == "" or path == "/":
            return path
        pathlist = path.split("/")
        stack = []
        for i in pathlist:
            if i == "":    
                if len(stack)==0:
                    stack.append("/")  
            elif i == "..":
                if len(stack) != 1:
                    if len(stack)>2:
                        stack.pop()
                    stack.pop()
            elif i != ".":  
                if stack[-1] != "/":
                    stack.append("/")            
                stack.append(i)
        res = ""
        if len(stack)==0:
            res = "/"
        else:
            if len(stack)>1 and stack[-1] == "/":
                stack.pop()
            while len(stack)> 0:
                res=stack.pop()+res
        return res
A = Solution()
path = "/.../"
s1="/a/../../b/../c//.//"
s2="/a//b////c/d//././/.."
s3 = "/home/"
s4="/a"
s5=""
s6="/ "
s7 = "/../"
s8 = "/a/./b/../../c/"
print(A.simplifyPath(s))
"""
    def simplifyPath(self, path):
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)
"""
               


