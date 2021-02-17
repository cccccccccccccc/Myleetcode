from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count= Counter(words)
        t = count.keys().map(lambda x:(-count.get(x),x))
        print(t)
        return heapq.nsmallest(k,count.keys(),key=lambda x:(-count.get(x),x))
A = Solution()
w = ["aaa","aa","a"]
k=3
print(A.topKFrequent(w,k))