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
A = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(A.reorderLogFiles(logs))

#["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]