class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        wordset = set()

        for c in s:
            if c in wordset:
                wordset.remove(c)
            else:
                wordset.add(c)
        return len(wordset)<=1
A = Solution()
s = "aab"
print(A.canPermutePalindrome(s))