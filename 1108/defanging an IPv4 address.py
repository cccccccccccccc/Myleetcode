"""timecomplexity = O(N) spacecomplexity = O(N)
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        res = ""
        for i in address:
            if i == ".":
                res+= '[.]'
            else:
                res+=i
        return res
"""
return '[.]'.join(i if i != '.' else [.] for i in address)
return address.replace('[.]','.')
"""

A = Solution()
a = "1.1.1.1"
print(A.defangIPaddr(a))