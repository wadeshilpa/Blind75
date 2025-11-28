# Difficulty : Medium
# Given a sorted array of unique elements that has been rotated, return the minimum element. 
# The algorithm must run in O(logn) time.

# Input: nums = [3, 4, 5, 1, 2]         Output: 1
# Input: nums = [4, 5, 6, 7, 0, 1, 2]   Output: 0
# Input: nums = [11, 13, 15, 17]        Output: 11

# Edge cases : empty array list, Single element, non-rotated array, negative numbers
# Time Complexity : O(log n)
# Space Complexity : O(1) 
# Worst Case : The rotation point is in the middle, requiring a full binary search.
# Best Case : The array is not rotated, allowing the minimum to be found immediately.

# class Solution:
#     def minSortedArray(self, nums:list[int]) -> int:

#         for i in range(1,len(nums)):
#             if nums[i] < nums[i-1]:
#                 return nums[i]
        
#         return nums[0]
# if __name__ =='__main__':
#     nums = list(map(int,input("enter nums").split(",")))
#     answer = solution().minSortedArray(nums)
#     print(answer)  

class Solution:
    def minSortedArray(self, nums:list[int])-> int:
        n=len(nums)
        left, right = 0, n-1

        if n==0:
            return None

        if nums[left] <= nums[right]:
            return nums[left]
        
        while left <= right:
            mid = (left + right)//2

            if nums[mid] > nums[mid+1] and mid < right:
                return nums[mid+1]
            if nums[mid-1] > nums[mid] and mid > left:
                return nums[mid] 

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
if __name__ == '__main__':
    nums=list(map(int,input("enter nums").split(",")))
    print(Solution().minSortedArray(nums))
