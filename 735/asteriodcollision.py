from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        starstack = []
        for i in asteroids:
            tmp = 1
            while starstack and starstack[-1]>0 and i < 0:
                if abs(i)>starstack[-1]:
                    starstack.pop()
                elif abs(i) == starstack[-1]:
                    starstack.pop()
                    tmp = 0
                    break
                else:
                    tmp = 0
                    break
            if tmp:
                starstack.append(i)
        return starstack
A = Solution()
a = [10,2,-5]
print(A.asteroidCollision(a))