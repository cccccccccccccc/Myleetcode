from typing import List
from collections import defaultdict
import collections
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scoredict = defaultdict(list)
        for i in items:
            scoredict[i[0]].append(i[1])
        result = []
        for key in scoredict:
            sum = 0
            for j in sorted(scoredict[key],reverse = True)[:5]:
                sum+=j
            result.append([key,sum//5])
        return sorted(result)
A = Solution()
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(A.highFive(items))