from typing import List
from collections import defaultdict
import heapq
class Trie:
    def __init__(self):
        self.node = defaultdict(Trie)
        self.list = []
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.sentencedict = {}
        self.root = Trie()
        for i, s in enumerate(sentences):
            self.insert(s,times[i])
        self.search = self.root
        self.new = ""
        self.ismiss = False
    def insert(self, s,t):
        self.sentencedict[s]= t
        cur = self.root
        for w in s:
            cur = cur.node[w]
            cur.list.append(s)
    def input(self, c: str) -> List[str]:
        answer = []
        if c == "#":
            if self.new != "":
                if self.new in self.sentencedict.keys():
                    self.sentencedict[self.new] +=1
                else:
                    self.insert(self.new,1)
            self.new = ""
            self.search = self.root
            self.ismiss = False
            return answer
        self.new+=c       
        if self.ismiss == True:
            return answer
        if c in self.search.node.keys():
            self.search = self.search.node[c]
            timeheapq = []
            heapq.heapify(timeheapq)
            for s in self.search.list:
                heapq.heappush(timeheapq,(-self.sentencedict[s],s))
            i = 0
            while i <3 and len(timeheapq)>0:
                answer.append(heapq.heappop(timeheapq)[1])
                i+=1
            return answer
        else:
            self.ismiss = True
            return answer
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
#["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input","input","input"]
#[[["abc","abbc","a"],[3,3,3]],["b"],["c"],["#"],["b"],["c"],["#"],["a"],["b"],["c"],["#"],["a"],["b"],["c"],["#"]]
A = AutocompleteSystem(["abc","abbc","a"],[3,3,3])
print(A.input("b"))
print(A.input("c"))
print(A.input("#"))
print(A.input("b"))
print(A.input("c"))
print(A.input("#"))
print(A.input("a"))
print(A.input("b"))
print(A.input("c"))
print(A.input("#"))
print(A.input("a"))
print(A.input("b"))
print(A.input("c"))
print(A.input("#"))



