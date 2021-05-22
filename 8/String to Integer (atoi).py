"""
time complexity = O(n) space complexity = O(1)
set MAX and MIN value to be 32 bits maximun and minimun integar 
strip to delete whitespace 
remain sign as 1 or -1 
check each char should be in '0'~ '9'
plus the ret as each bit  check MAX//10 and ret to make sure result will not out of range
return ret*sign
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        ls = s.strip()
        if len(ls) == 0 :
            return 0
        i=0
        ret = 0
        sign = 1
        MAX = 2147483647
        MIN = -2147483648
        if ls[i] =='+' or ls[i] == '-':
            sign = 1-2*(ls[i] == '-')
            i+=1
        while i<len(ls) and ls[i]>='0'and ls[i]<='9':
            if ret > MAX//10 or (ret == MAX//10 and ord(ls[i])-ord('0') > MAX%10):
                return MAX if sign ==1 else MIN
            ret = ret*10+ (ord(ls[i])-ord('0'))
            i+=1
        return ret*sign
A = Solution()
s = "2147483648"
print(A.myAtoi(s))