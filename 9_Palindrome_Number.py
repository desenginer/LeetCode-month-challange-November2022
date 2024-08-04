#https://leetcode.com/problems/palindrome-number
"""
Given an integer x, return true if x is a palindrome
, and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        stry = strx[::-1]
        if strx == stry:
            return 1
        else:
            return 0