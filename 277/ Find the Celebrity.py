# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebritycandidate = 0
        for i in range(1,n):
            if knows(celebritycandidate,i):
                celebritycandidate = i
        for j in range(n):
            if celebritycandidate == j:
                continue
            if knows(celebritycandidate,j) or !knows(j,celebritycandidate):
                return -1
        return celebritycandidate