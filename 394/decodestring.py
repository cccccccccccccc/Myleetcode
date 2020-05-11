class Solution: 
    def decodeString(self, s: str) -> str:
        self.i =0
        return self.getdecodeString(s)       
    def getdecodeString(self, s: str) -> str:
        if len(s) == 0:
            return ""
        count = 0
        curstr = ''
        while self.i < len(s):
            tmpi = self.i
            self.i+=1
            if ord(s[tmpi])>=ord('0') and ord(s[tmpi])<=ord('9'):
                count = int(s[tmpi]) if count == 0 else count*10+int(s[tmpi])
            elif s[tmpi] == "[":
                curstr += count*self.getdecodeString(s)
                count = 0
            elif s[tmpi] == "]":
                return curstr
            else:
                curstr += s[tmpi]
        return curstr
                
        
A = Solution()
a = "3[a]2[bc]"# return "aaabcbc".
b = "3[a2[c]]"# return "accaccacc".
c = "2[abc]3[cd]ef"#, return "abcabccdcdcdef".
d = "abc"
e = "1[abc]"
f = "[]"
print(A.decodeString(a))
print(A.decodeString(b))
print(A.decodeString(c))
print(A.decodeString(d))
print(A.decodeString(e))
print(A.decodeString(f))

"""
for i in range(len(s)):
            if ord(s[i])>=ord('1') and ord(s[i])<=ord('9'):
                count = int(s[i]) if count == 0 else count*10+int(s[i])
            elif s[i] == '[' :
                if len(curstr) != 0:                
                    count = 1 if count == 0 else count
                    return curstr*count+self.decodeString(s[i+1:])
            elif s[i] == ']':
                
            else:
                curstr+=s[i]
        return curstr if curstr != "" else ""
"""