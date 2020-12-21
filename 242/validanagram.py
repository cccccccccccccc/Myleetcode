from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(list(s))
        b = sorted(list(t))
        if len(a)!= len(b):
           return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
A = Solution()
s = "anagram"
t = "nagaram"
print(A.isAnagram(s,t))