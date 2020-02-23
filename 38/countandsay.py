"""
timecomplexity = O(n*m) m is string's length, spacecomplexity = O(m)
iterate n call construct func to get every sequence string 
in the function iterate the string 
if s[i] == s[i+1] update count continue 
else update count and current char to tmpstring 
remember to add the last char in s to tmpstring 


"""
class Solution:
    def countAndSay(self, n: int) -> str:
        def countandsayonce(S):
            tmpstr = ''
            count = 1
            for i in range(len(S)-1):
                if S[i] ==S[i+1]:
                    count+=1
                    continue
                else:
                    tmpstr+= str(count)+S[i]
                    count = 1
            tmpstr += str(count)+S[-1]
            return tmpstr
        result = '1'
        for _ in range(n-1):
            result = countandsayonce(result)
        return result
A = Solution()
print(A.countAndSay(6))
