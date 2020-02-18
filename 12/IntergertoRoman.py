"""
timecomplexity = O(1) spacecomplexity = O(1)
define a list to contain all special interger in Roman, a string list of all Roman numerals include special numerals
and make sure these two lists' value are the same and from large to small 
iterate and enumerate the value use the index and value to construct the Roman numerals
first let the numeber // by value the reslut * roman numerals ,add to result
then update number % value 
continue to the end
return result
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ""
        for i, v in enumerate(value):
            res += num//v*numerals[i]
            num = num%v
        return res