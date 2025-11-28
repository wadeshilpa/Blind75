# Medium
# Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]       Output: 6
# Input: nums = [1]                           Output: 1
# Input: nums = [5,4,-1,7,8]                  Output: 23

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################

class Solution:
    def maxSubArray(self, nums:list[int])->int:
        if not nums:
            return 0
        
        currentMax = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            currentMax = max(num, currentMax+num)
            maxSum = max(maxSum, currentMax)

        return maxSum
if __name__ == "__main__":
    nums = list(map(int,input("Enter comma separated numbers = ").split(",")))
    result = Solution().maxSubArray(nums)
    print("Output = ", str(result))