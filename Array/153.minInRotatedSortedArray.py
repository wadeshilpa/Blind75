# Medium
# Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

# Input: nums = [3,4,5,1,2]           Output: 1
# Input: nums = [4,5,6,7,0,1,2]       Output: 0
# Input: nums = [11,13,15,17]         Output: 11

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################

class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            return None
        
        n = len(nums)
        if n == 1 or (nums[0] < nums[n-1]):
            return nums[0]
        
        left, right = 0, (n-1)
        
        while left < right:
            mid = (right + left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
    
if __name__ == "__main__":
    nums = list(map(int,input("Enter comma separated values = ").split(',')))
    print(Solution().findMin(nums))