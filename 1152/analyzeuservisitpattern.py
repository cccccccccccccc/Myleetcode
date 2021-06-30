"""
n is log number
timecomplexity = O(n**3) spacecomplexity = O(n)
depend on timestamp sort the website and get user website dict,we can use zip to get list of tuple then sort them by time
each user get all possible threeseq so iterate website the user visit by userwebdict  
because user can visit the same website many times so avoid duplicate sequance, we need to use a curset to maysure this user didnt appear this sequarnce before 
check tmpseq if it is appear before and if not add to set and three seq 
get item in threedict sort by user num and lexicographically 
"""
from typing import List
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        userwebdict = defaultdict(list)
        for t,u,w in sorted(zip(timestamp,username,website)):
            userwebdict[u].append(w)
        threeseq = {}
        for u in userwebdict.keys():
            curset = set()
            curweb = userwebdict[u]
            for i in range(len(curweb)):
                for j in range(i+1,len(curweb)):
                    for r in range(j+1,len(curweb)):
                        tmpseq = (curweb[i],curweb[j],curweb[r])
                        if tmpseq in threeseq:
                            if tmpseq not in curset:
                                threeseq[tmpseq]+=1
                                curset.add(tmpseq)
                        else:
                            threeseq[tmpseq]=1
                            curset.add(tmpseq)
        ans = list(threeseq.items())
        ans.sort(key=lambda x:(-x[1],x[0]))
        return ans[0][0]


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

