"""
timecomplexity = O(n*m) n is length of logs m is identifier in each log, worset m is length of each logs[i].length-2
separate original log list into two lists one is lettersublist the other is digitsublist.
iterate logs check the first element after space' ' is letter consist it as a tuple first is log contents second is log identifier third is the whole log
sort lettersublist 
iterate it to get new letterlist by lettersublist[2]
return letterlist+digitsublist
"""
"""
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitsublist = []
        lettersublist = []
        for l in logs:
            for s in range(len(l)):
                if l[s] == " ":
                    if l[s+1]>='a'and l[s+1]<='z':
                        lettersublist.append((l[s+1:],l[:s],l))
                        break
                    else:
                        digitsublist.append(l)
                        break
        lettersublist.sort()
        letterlist = []
        for i in lettersublist:
            letterlist.append(i[2])
        return letterlist+digitsublist
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lettersublist = []
        digitsublist = []
        for l in logs:
            for i in range(len(l)):
                if i == " ":
                    if l[i+1] >= 'a' and l[i+1]<= 'z':
                        lettersublist.append((l[i+1:],l[:i],l))
                        break
                    else:
                        digitsublist.append(l)
                        break
        lettersublist.sort()
        letter = []
        for i in lettersublist:
            letter.append(lettersublist[i][2])
        return letter+digitsublist
A = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(A.reorderLogFiles(logs))

#["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]