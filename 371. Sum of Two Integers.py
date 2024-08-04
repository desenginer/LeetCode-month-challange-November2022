#https://leetcode.com/problems/sum-of-two-integers
'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= 0x7FFFFFFF else ~(a ^ mask)