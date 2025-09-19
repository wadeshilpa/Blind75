# Medium
# Search in Rotated Sorted Array
# binary search

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) 
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [4,5,6,7,0,1,2], target = 0       Output: 4
# Input: nums = [4,5,6,7,0,1,2], target = 3       Output: -1
# Input: nums = [1],             target = 0       Output: -1

# Edge cases        : 
# Time Complexity   : O(log n)
# Space complexity  : O(1) (just pointers)
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def searchInRotatedSortedList(self, nums:list[int], target:int)-> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
if __name__ == "__main__":
    nums = list(map(int,input("Enter nums array = ").split(",")))
    target = int(input("enter target = "))
    print(Solution().searchInRotatedSortedList(nums, target))


            