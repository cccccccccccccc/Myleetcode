#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.worddict = defaultdict(TrieNode)
        self.wordlist = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        word = word.lower()
        current = self.root
        for i in word:
            current = current.worddict[i]
            current.wordlist.append(word)
    def search(self,word):
        word = word.lower()       
        current = self.root
        ans = []
        for i,c in enumerate(word):
            if c in current.worddict.keys():
                current=current.worddict[c]
                if i >=1:
                    print(current.wordlist)
                    ans.append(current.wordlist[0:3])
            else:
                break
        return ans
    

def searchSuggestions(repository, customerQuery):
    print(customerQuery)
    print(repository)
    # Write your code here
    root = Trie()
    lowerrepo = []
    for w in repository:
        lowerrepo.append(w.lower())
    lowerrepo.sort()
    print(lowerrepo)
    for w in lowerrepo:
        root.insert(w)
    return root.search(customerQuery)
    

if __name__ == '__main__':