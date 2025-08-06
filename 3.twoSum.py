# Difficulty : Easy
# Two Sum
# Hash Map / Dictionary Lookup

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9     Output: [0,1]

# Input: nums = [3,2,4], target = 6         Output: [1,2]

# Input: nums = [3,3], target = 6           Output: [0,1]

# Edge cases : negative numbers, empty array list, Single element
# Time Complexity : O(n)
# Space Complexity : O(n) because dictionary is being used which will store (n-1) key value pairs in worst case
# Worst Case : When two numbers that sum up to the target are present at the very end of the array
# Best Case : When first two elements add upto the target
########################################################################
class solution:
    def twoSum(self, nums:list[int], target:int)->list[int]:
        num_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in num_dict:
                return [num_dict[diff], i]

            num_dict[num] = i

        return []

if __name__ == "__main__":
    nums = list(map(int,input("enter an array of integers = ").split(",")))
    target = int(input("enter target value = "))
    print(solution().twoSum(nums, target))

