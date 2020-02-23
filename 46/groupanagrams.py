"""
timecomplexity = O(n*m) n=len(strs),m=len(s) s is item in strs spacecomplexity = O(n+m)
construct deflautdict deflautdict is a method from moudle collections can easy to use append() from List 
use the deflautdict to contain result. iterate all s in strs, define tmp list count [0]*26, iterate every word in s 
and do ord(c)-ord('a') let the result tobe count's index and add 1 to index
trans the count list into tuple and let it be dict's key and append the s  Because tuple can be compared by the whole item.
finally return all res.values()
"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return res.values()
A = Solution()
a = ["eat","tea","tan","ate","nat","bat"]
print(A.groupAnagrams(a))