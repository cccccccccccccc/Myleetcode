from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) ==0:
            return ""
        letter = defaultdict(list)
        topo = defaultdict(list)
        sortdeque = deque()
        for s in words:
            for i in s:
                letter[i] = 0
        for j in range(len(words)-1):
            curlen = min(len(words[j]),len(words[j+1]))
            for m in range(curlen):
                if words[j][m]!=words[j+1][m]:
                    topo[words[j][m]].append(words[j+1][m])
                    letter[words[j+1][m]]+=1
                    break
                elif len(words[j])>len(words[j+1]) and m == curlen-1:
                    return ""
        for k in letter.keys():
            if letter[k] == 0:
                sortdeque.append(k)
        ans = ""
        while len(sortdeque)!=0:
            curletter = sortdeque.popleft()
            ans+=curletter
            for n in topo[curletter]:
                letter[n]-=1
                if letter[n] == 0:
                    sortdeque.append(n)

        if len(ans) != len(letter.keys()):
            return ""
        else:
            return ans
A = Solution()
words = ["wrt","wrf","er","ett","rftt"]
abc = ["abc","ab"]
error = ["qb","qts","qs","qa","s"]
print(A.alienOrder(error))
