from typing import List
class Solution:
    def _wordbreak(self,s,wordset):
        if s not in self.memoryword:
            for i in range(0,len(s)):
                left = s[0:i]
                right = s[i::]
                if right in wordset and self._wordbreak(left,wordset):
                    self.memoryword[s] = True
                    break
                else:
                    self.memoryword[s] = False
        return self.memoryword[s]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memoryword = {}
        self.memoryword[""] = True
        wordset = set(wordDict)
        return self._wordbreak(s,wordset)
A = Solution()
a = "leetcode"
c = ""
d = "leet"
e = "leetleet"
b = ["leet", "code"]
print(A.wordBreak(a,b))