# Easy
# Missing Number
# XOR
# https://leetcode.com/problems/missing-number/description/

# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Input: nums = [3,0,1]                   Output: 2
# Input: nums = [0,1]                         Output: 2
# Input: nums = [9,6,4,2,3,5,7,0,1]           Output: 8

########################################################################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_set = set(nums)

        for i in range(len(nums)+1):
            if i not in nums_set:
                return i

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing = len(nums)

        for i, num in enumerate(nums):
            missing = missing ^ i ^ num

        return missing