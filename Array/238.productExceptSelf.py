# Medium
# Product of Array Except Self
# Array

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]             Output: [24,12,8,6]
# Input: nums = [-1,1,0,-3,3]         Output: [0,0,9,0,0]
# Input: nums = [3,3,3,3]             Output: [27,27,27,27]
# Input: nums = [0,0,2,3]             Output: [0,0,0,0]
# Input: nums = [2, 5, 6, 7]          Output: [210, 84, 70, 60]

# Edge Case : empty, sigle element, negative numbers
# Time Complexity : O(n)
# Space Complexity : only one array (result),  O(1) extra space
# Best Case  : O(n) ; because the iterations are inevitable
# Worst Case : O(n) ; same reason
# Average Case : O(n) ; same reason
########################################################################
class Solution:
    def productExceptSelf(self,nums:list[int])->list[int]:
        if not nums or len(nums)<2:
            return []
        
        n=len(nums)
        result=[1]*n

        for i in range(1,n):
            result[i] = result[i-1] * nums[i-1]

        product=1

        for i in range(n-1,-1,-1):
            result[i] = result[i] * product
            product = product * nums[i]

        return result

if __name__=='__main__':
    try:
        nums=list(map(int,input("Enter comma-separated integers: ").split(",")))
        answer=Solution().productExceptSelf(nums)
        print("Output : " + str(answer))
    except ValueError:
        print("Invalid input")
    