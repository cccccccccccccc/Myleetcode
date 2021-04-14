from collections import defaultdict
from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x:len(x))
        worddict = defaultdict(list)
        cword = []
        for w in words:
            worddict[w[0]].append(w)
        for w in words:
            tmp = 0
            for i in range(len(w)):
                for miniword in worddict[w[i]]:
                    if len(miniword) <= len(w)-i and miniword == w[i:i+len(miniword)+1]:
                        tmp+=1
                        if tmp==2:
                            break
                if tmp == 2:
                    cword.append(w)
                    break
        
        return cword
A = Solution()
a = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(A.findAllConcatenatedWordsInADict(a))