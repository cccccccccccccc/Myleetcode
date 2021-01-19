from typing import List
from collections import defaultdict
class DSU():
    def __init__(self):
        self.paremail = {}
        self.rank = defaultdict(list)
    def find(self,s):
        if s not in self.paremail.keys():
            self.paremail[s] = s
            self.rank[s] = 1
        if s != self.paremail[s]:
            self.paremail[s] = self.find(self.paremail[s])
        return self.paremail[s]
    def union(self,s1,s2):
        s1p = self.find(s1)
        s2p = self.find(s2)
        if s1p != s2p :
            if self.rank[s1p]>self.rank[s2p]:
                self.paremail[s2p] = s1p
            elif self.rank[s1p]<self.rank[s2p]:
                self.paremail[s1p] = s2p
            else:
                self.paremail[s1p] = s2p
                self.rank[s2p] +=1
    def get (self):
        emaildict = defaultdict(list)
        for e in self.paremail.keys():
            emaildict[self.find(e)].append(e)
        return emaildict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailtoname = defaultdict(list)
        emaildsu = DSU()
        for acnt in accounts:
            for e in range(1,len(acnt)):
                emailtoname[acnt[e]]=acnt[0]
            if len(acnt)>=2:
                for i in range(1,len(acnt)):
                    emaildsu.union(acnt[1],acnt[i])
        emaildict = emaildsu.get()
        acntmerge = []
        for e in emaildict.keys():
            acntmerge.append([emailtoname[e]]+ sorted(emaildict[e]))
        return acntmerge

A = Solution()
a = accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(A.accountsMerge(a))


