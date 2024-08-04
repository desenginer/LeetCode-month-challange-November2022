#https://leetcode.com/problems/delete-columns-to-make-sorted-ii
'''
You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.
'''


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        tpse, n, m = zip(*strs), len(strs), len(strs[0])
        strs = [''] * n

        for nxt in tpse:
            temp = [strs[i] + nxt[i] for i in range(n)]
            if temp == sorted(temp): strs = temp

        return m - len(strs[0])