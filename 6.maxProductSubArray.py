# Medium
# Maximum Product Subarray

# Given an integer array nums, find a  subarray that has the largest product, and return the product.
# Subarray : contiguous non-empty sequence of elements within an array.
# The test cases are generated so that the answer will fit in a 32-bit integer.

# Input: nums = [2,3,-2,4]                  Output: 6
# Input: nums = [2,3,-2,4,-1]               Output: 48
# Input: nums = [-2,0,-1]                   Output: 0
# Input: nums = [-1, -2, -3, 0]             Output:6
# Input: nums = [0, 2, -1, -3, 5, -4]       Output:60
# Input: nums = [2, -5, 3, 1, -4]           Output:60
# Input: nums = [1, 0, -1, 2, 3, -5, -2]    Output:60

class solution:
    def maxProductSubArray(self,nums:list[int])->int:
        current_max = current_min = result = nums[0]
       
        for num in nums[1:]:
            temp_max = max(num, current_max*num, current_min*num)
            temp_min = min(num, current_max*num, current_min*num)
            current_max=temp_max
            current_min=temp_min
            result=max(result,current_max)
        return result
    
if __name__=='__main__':
    nums=list(map(int,input("Enter nums array").split(",")))
    answer=solution().maxProductSubArray(nums)
    print(answer)