from typing import List
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        userdict = collection.defaultdict(List)
        for t,u,w in sorted(zip(timestamp,username,website)):
            userdict[u].append(w)
        threeseq = {}
        for user in userdict:
            curset = set()
            cur = userdict[user]
            cur.sort(key = lambda x:x[0])
            for i in range(len(cur)):
                for j in range(i+1,len(cur)):
                    for k in range(j+1,len(cur)):
                        tmpseq = (cur[i][1],cur[j][1],cur[k][1])
                        if tmpseq in threeseq:
                            if tmpseq not in curset:
                                threeseq[tmpseq] +=1
                                curset.add(tmpseq)
                        else:
                            threeseq[tmpseq]= 1
                            curset.add(tmpseq)
        ans = list(threeseq.items())
        ans.sort(key= lambda x: (-x[1], x[0]))
        return list(ans[0][0])
A = Solution()
username =["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

a=["dowg","dowg","dowg"]
b=[158931262,562600350,148438945]
c=["y","loedo","y"]

a = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
b = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
c = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
print (A.mostVisitedPattern(a,b,c))