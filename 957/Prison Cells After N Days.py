from collections import defaultdict
from typing import List
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        dictcell = {}
        last= 0
        nextcell = []
        for d in range(n):
            key = ""
            nextcell = []
            for i in range(len(cells)):
                if i == 0 or i == 7:
                    nextcell.append(0)
                    key+=str(0)
                else:
                    tmp = (cells[i-1]+cells[i+1]+1)%2     
                    nextcell.append(tmp)
                    key+=str(tmp)
            cells = nextcell
            if key in dictcell.keys():
                print(dictcell[key])
                last = (n-d-1)%(d+1-dictcell[key])
                break
            else:
                dictcell[key] = d + 1         
        if last !=0:
            for d in range(last):
                nextcell =[]
                for i in range(len(cells)):
                    if i == 0 or i == 7:
                        nextcell.append(0)
                    else:
                        tmp = (cells[i-1]+cells[i+1]+1)%2     
                        nextcell.append(tmp)
                cells = nextcell
        return cells
A = Solution()
cells = [1,0,0,1,0,0,1,0]
n = 14
# print(A.prisonAfterNDays(cells,n))
cells = [1,0,0,1,0,0,1,0]
n = 28
print(A.prisonAfterNDays(cells,n))