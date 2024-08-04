#https://leetcode.com/problems/count-primes
'''
Given an integer n, return the number of prime numbers that are strictly less than n.
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [1] * n
        for i in range(2, int(n**0.5) + 1):
            if prime[i] == 1:
                for j in range(i*i, n, i):
                    prime[j] = 0

        ans = 0
        for i in range(2, n):
            if prime[i] == 1:
                ans += 1

        return ans
