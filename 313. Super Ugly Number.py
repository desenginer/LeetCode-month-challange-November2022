#https://leetcode.com/problems/super-ugly-number
'''
A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        super_ugly = [1]
        idx = [0] * len(primes)
        prod = [p for p in primes]

        while len(super_ugly) < n:
            next_ugly = min(prod)
            super_ugly.append(next_ugly)
            for i in range(len(primes)):
                if next_ugly == prod[i]:
                    idx[i] += 1
                    prod[i] = primes[i] * super_ugly[idx[i]]

        return super_ugly[-1]