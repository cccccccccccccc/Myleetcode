from typing import List

"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emaildict = {}
        for address in emails:
            tmpadr =''
            isdelete = False
            i = 0
            while i <len(address):
                if isdelete == True and address[i] != '@':
                    i+=1
                    continue
                elif address[i] == '+':
                    isdelete = True
                elif address[i] == '.':
                    i+=1
                    continue
                elif address[i] == '@':
                    tmpadr+=address[i:]
                    break
                else:
                    tmpadr+=address[i]
                i+=1
            if tmpadr in emaildict:
                emaildict[tmpadr]+=1
            else:
                emaildict[tmpadr] = 1

        return len(emaildict.keys())
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailset = set()
        for email in emails:
            local,domain = email.split('@')
            real_local = local.split('+')[0].replace('.','')
            emailset.add(real_local+'@'+domain)
        return len(emailset)

A = Solution()
a = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
b = ["a.b++@gg.c","a..b+-@g.g.c"]
print(A.numUniqueEmails(a))