from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.node = defaultdict(TrieNode)
        self.isword = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for i in word:
            current = current.node[i]
        current.isword = True

    def search(self, word: str) -> bool:
        def search_in_word(word,trie)->bool:
            for i, w in enumerate(word):
                if w not in trie.node.keys():
                    if w == ".":
                        for x in trie.node:
                            if search_in_word(word[i+1:],trie.node[x]):
                                return True
                    return False
                else:
                    trie = trie.node[w]
            return trie.isword
        return search_in_word(word,self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
A = WordDictionary()
print(A.addWord("add"))
print(A.search(".dd"))