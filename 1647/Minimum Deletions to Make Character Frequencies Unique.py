from collections import defaultdict
from typing import List
class Solution:
    def minDeletions(self, s: str) -> int:
        letternum = [0]*26
        letterdict = defaultdict(list)
        frequency = []
        for c in s:
            letternum[ord(c)-ord('a')]+=1
        for i in range(len(letternum)):
            if letternum[i]>0:
                letterdict[letternum[i]].append(i)
        for k in letterdict.keys():
            frequency.append((len(letterdict[k]),k))
        frequency.sort()
        letterset = set()
        num = 0
        for t in frequency:
            tmpn = t[0]
            for _ in range(tmpn):
                tmpf = t[1]
                if tmpf not in letterset or tmpf == 0:
                    letterset.add(tmpf) 
                else:
                    while tmpf >=0:
                        num+=1
                        tmpf-=1
                        if tmpf not in letterset or tmpf == 0:
                            letterset.add(tmpf)
                            break
        return num
A = Solution()
s = "ceabaacb"
print(A.minDeletions(s))