#https://leetcode.com/problems/maximum-gap
'''
Given an integer array nums, return the maximum difference between two
successive elements in its sorted form. If the array contains less than
 two elements, return 0.
You must write an algorithm that runs in linear time and uses linear
extra space.
'''


class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        nums.sort()
        maxDiff = 0

        for i in range(1, len(nums)):
            maxDiff = max(maxDiff, nums[i] - nums[i - 1])

        return maxDiff