#timecomplexity = O(n), spacecomplexity = O(n)
"""
from left do iterate to count if change s[0]to s[i] into 0,need how many changes,
from right do iterate to count if change s[-1]to s[i] into 1 , need how many changes
then iterate S to get minimum ans l[i-1]+r[i]
remember two special case :l[len(S)-1], r[0]
"""
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        l = [0]*len(S)
        r = [0]*len(S)
        l[0] = ord(S[0])-ord('0')
        r[-1] = ord('1') - ord(S[-1])
        for i in range(1,len(S)):
            l[i] = l[i-1]+ ord(S[i])-ord('0')
        for j in range(len(S)-2,-1,-1):
            r[j] = r[j+1]+ord('1') - ord(S[j])
        ans = min(l[len(S)-1],r[0])
        for i in range(1,len(S)):
            ans = min(ans,l[i-1]+r[i])
        return ans
A = Solution()
a = "00110"
print(A.minFlipsMonoIncr(a))