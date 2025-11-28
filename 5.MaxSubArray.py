# Medium 
# Maximum Subarray

# Given an integer array nums, find the  subarray with the largest sum, and return its sum.
# Subarray - A subarray is a contiguous non-empty sequence of elements within an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]    Output: 6
# Input: nums = [1]                        Output: 1
# Input: nums = [5,4,-1,7,8]               Output: 23
# Input: nums = [-8, -3, -6, -2, -5, -4]   Output: -2
# Input: nums = [-1]                       Output: -1

# Time complexity : O(n)
# Space Complexity : O(1)
# Edge Cases : empty, single, single negative, multiple negative
# Best Case : O(n)
# Worst Case : O(n)
# Average Case : O(n)

class solution:
    def maxSubArray(self,nums:list[int])->int:
        prev=max_sum=nums[0]

        for num in nums[1:]:

            if num >= (prev + num):
                prev = num
            else:
                prev = (prev + num)

            # prev = max(prev,prev+num)   --Above 4 lines can be replaced with this
            max_sum=max(max_sum , prev)

        return max_sum

if __name__ == '__main__':
    try:
        nums=list(map(int,input("Enter nums array = ").split(",")))
        answer=solution().maxSubArray(nums)
        print(answer)
    except ValueError:
        print("Invalid Input")

  