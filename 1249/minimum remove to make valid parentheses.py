class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        fistparsestring = []
        balance = 0
        open_parenthese_found = 0
        for c in s:
            if c == '(':
                balance +=1
                open_parenthese_found += 1
            if c == ')':
                if balance == 0:
                    continue
                balance-=1
            fistparsestring.append(c)
        result = []
        open_parenthese_keep = open_parenthese_found - balance
        for i in fistparsestring:
            if i == '(':
                open_parenthese_keep -= 1
                if open_parenthese_keep < 0:
                    continue
            result.append(i)
        return "".join(result)
A = Solution()
s = ["a",")","b","(","c",")","d"]
s1 = ["l","e","(","t","(",")",")",")"]
s2 = [")",")","(","("]
s3 = ["(","a","(","b","(","c",")","d",")"]
s4 = ["(","("]
print(A.minRemoveToMakeValid(s3))