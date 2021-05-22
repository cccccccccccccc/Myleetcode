"""
timecomplexity = O(n),spacecomplexity = O(n)
negative integar is not Palindrome because sign will be different between orignal one and reverse one. So check the x <0 False if 0<=x<10 because it reverse is still  itself
so it is true. 
use a list to remain each bit in the integar. take the divisor of x put in list, take the remainder of x and use it as next time x
untill the divisor is 0 remain the len of the integar x 

get the result by cmp two sides of the list depending on  len is odd or even.

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<10 and x>=0:
            return True
        elif x<0:
            return False
        divisor = x
        listnum = []
        len =0
        while divisor != 0:
            listnum.append(divisor%10)
            divisor= divisor//10
            len+=1
        if len%2 != 0:
            return listnum[0:len//2] == listnum[len//2+1:][::-1]
        else:
            return listnum[0:len//2] == listnum[len//2:][::-1]
A = Solution()
x = -121
print(A.isPalindrome(x))