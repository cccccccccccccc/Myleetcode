class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        transform = {}
        for i in range(len(str1)):
            if str1[i] not in transform.keys():
                transform[str1[i]] = str2[i]
            elif transform[str1[i]]!= str2[i]:
                return False
        return len(set(str2))<26
A = Solution()
str1 = "aabcc"
str2 = "ccdee"
print(A.canConvert(str1,str2))