from collections import deque
class Solution:
    def isVaildTag(self, i ,s):
        maxindex = i+8
        name = ""
        while i < min(len(s),maxindex):
            if s[i]>='A'and s[i]<="Z":
                name+=s[i]
            elif s[i] == '>':
                return name
        return ""
            
    def isValid(self, code: str) -> bool:
        if len(code)<7:
            return False
        tagdeque = deque()
        if s[0]!= "<":
            return False
        index = 1
        tagname = self.isVaildTag(index,code)
        if tagname == ""
            return False
        else:
            tagdeque.append((1,tagname))
        while len(tagdeque)!= 0:
            