class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 =='0':
            return '0'
        if len(num1)<len(num2):
            num1,num2 = num2,num1
        numdict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        tmp1 = num1[::-1]
        tmp2 = num2[::-1]
        newnum = [0]*(len(tmp1)+len(tmp2))
        for i,n2 in enumerate(tmp2):
            for j, n1 in enumerate(tmp1):
                pos = i+j
                newnum[pos]+= numdict[n1]*numdict[n2]
                newnum[pos+1] += newnum[pos]//10
                newnum[pos] = newnum[pos]%10
        res = ''.join(map(str,newnum[::-1]))
        m=0
        while m < len(res):
            if res[m] == '0':
                m+=1
            else:
                break
        return res[m:]
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:        
        tmp1 = tmp2 = 0
        int1 = int2 = 0
        while tmp1 < len(num1):
            int1 = int1*10 + ord(num1[tmp1])-ord('0')
            tmp+=1
        while tmp2 < len(num2):
            int2 = int2*10 + ord(num2[tmp2])- ord('0')
            tmp+=2
        return str(int1*int2)
"""
A =Solution()
print(A.multiply('123','456'))