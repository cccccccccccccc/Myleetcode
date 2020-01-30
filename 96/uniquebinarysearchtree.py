"""
Algorithm

The problem is to calculate the number of unique BST. To do so, we can define two functions:

G(n): the number of unique BST for a sequence of length n.
F(i,n): the number of unique BST, where the number i is served as the root of BST (1≤i≤n).
Later we would see that G(n) can be deducted from F(i,n), which at the end, would recursively refers to G(n).

First of all, following the idea in the section of intuition, we can see that the total number of unique BST G(n), is the sum of BST F(i,n) enumerating each number i (1 <= i <= n) as a root. i.e.

G(n) =∑i=1 n F(i,n)(1)

Particularly, for the bottom cases, there is only one combination to construct a BST out of a sequence of length 1 (only a root) or nothing (empty tree). i.e.

G(0)=1,G(1)=1

Given a sequence 1 ... n, we pick a number i out of the sequence as the root, then the number of unique BST with the specified root defined as F(i, n)F(i,n), 
is the cartesian product of the number of BST for its left and right subtrees, as illustrated below:

For example, F(3, 7), the number of unique BST tree with the number 3 as its root. To construct an unique BST out of the entire sequence [1, 2, 3, 4, 5, 6, 7] with 3 as the root, 
which is to say, we need to construct a subtree out of its left subsequence [1, 2] and another subtree out of the right subsequence [4, 5, 6, 7], 
and then combine them together (i.e. cartesian product). Now the tricky part is that we could consider the number of unique BST out of sequence [1,2] as G(2), 
and the number of of unique BST out of sequence [4, 5, 6, 7] as G(4). For G(n), it does not matter the content of the sequence, but the length of the sequence. 
Therefore, F(3,7) = G(2)⋅G(4). To generalise from the example, we could derive the following formula:

F(i,n)=G(i−1)⋅G(n−i)(2)

By combining the formulas (1), (2), we obtain a recursive formula for G(n)G(n), i.e.

G(n) =∑ i=1 n G(i−1)⋅G(n−i)(3)

timecomplexity = O(n^2) spacecomplexity = O(n)
""" 
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]