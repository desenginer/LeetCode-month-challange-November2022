#https://leetcode.com/problems/rotate-array/
'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = rotated[i]