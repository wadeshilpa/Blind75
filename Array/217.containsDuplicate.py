# Easy 
# Contains Duplicate
# array/ sets

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]                 Output: true
# Input: nums = [1,2,3,4]                 Output: false
# Input: nums = [1,1,1,3,3,4,3,2,4,2]     Output: true

# Edge cases        : empty list, single element, negative numbers
# Time Complexity   : O(n)
# Space complexity  : O(n)
# Best case         : O(1) if 2nd element is duplicate
# Worst Case        : O(n) Duplicate at the end, or no duplicate
########################################################################
class Solution:
    def containsDuplicate(self, nums:list[int])->bool:
        if not nums or len(nums) < 2:
            return False
        
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False 
    
if __name__ == '__main__':
    nums = list(map(int,input("Enter nums array = ").split(",")))
    print(Solution().containsDuplicate(nums))

