#https://leetcode.com/problems/word-break
'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True

    def getRoot(self):
        return self.root


class Solution:
    def wordBreak(self, s, wordDict):
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            node = trie.getRoot()
            for j in range(i, n):
                index = ord(s[j]) - ord('a')
                if node.children[index] is None:
                    break
                node = node.children[index]
                if node.isEndOfWord:
                    dp[j + 1] = True

        return dp[n]