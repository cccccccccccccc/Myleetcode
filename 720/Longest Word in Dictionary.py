from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordset = set(words)
        ans = ""
        for w in words:
            if len(w) > len(ans) or (len(w) == len(ans) and w < ans):
                if all(w[:k] in wordset for k in range(1,len(w))):
                    ans = w
        return ans
A = Solution()
w = ["w","wo","wor","worl", "world"]
print(A.longestWord(w))