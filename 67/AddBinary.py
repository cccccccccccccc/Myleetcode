"""
timecomplexity = O(max(len(a),len(b)) spacecomplexity = O(len(a)+len(b))
reverse a and b to c and d 
iterate the max length from a and b trun everyone into int
new str[i] = (c[i]+d[i])%2 and carry = (c[i]+d[i])//2
return str[::-1]
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a),len(b))
        c = a[::-1]
        d = b[::-1]
        tmp = 0
        res = ''
        i = 0
        def helper(i,s):
            if i < len(s):
                return s[i]
            else:
                return 0
        while i < maxlen:
            tmpc = int(helper(i,c))
            tmpd = int(helper(i,d))
            res+=str((tmpc+tmpd+tmp)%2 )      
            tmp = (tmpc+tmpd+tmp)//2
            i+=1
        if tmp!= 0 :
            res+=str(tmp)
        return res[::-1]
A = Solution()
a = '11'
b = '1'
print(A.addBinary(a,b))
"""
Approach 1:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
Approach 2:
class Solution:
    def addBinary(self,a: str, b: str) ->str:
        return format(int(a,2)+int(b,2),"b")
"""