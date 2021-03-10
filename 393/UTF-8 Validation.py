from typing import List
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        mask1 = 1<<7
        mask2 = 1<<6
        count = 0
        for d in data:
            mask = 1<<7
            while mask&d:
                mask>>=1
                count+=1
            if count ==0:
                continue
            if count = 1 or count > 4:
                return False
            else:
                if not(d&mask1 and not(d&mask2)):
                    return False
            count-=1
        return count == 1   