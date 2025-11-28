# Difficulty : Medium 
# Variant of TwoSum but the list is sorted. So the space complexity can be reduced to O(1) by using 2 pointers.

# Given a 1-indexed, sorted array of integers, find two numbers that add up to a specific target. 
# Return their indices as a list [index1, index2] where 1 <= index1 < index2 <= numbers.length. 
# Each test case has exactly one solution, and you cannot use the same element twice. 
# Use only constant extra space.

# Input: numbers = [2,7,11,15],   target = 9             Output: [1,2]
# Input: numbers = [2,3,4],       target = 6             Output: [1,3]
# Input: numbers = [-1,0],        target = -1            Output: [1,2]

# Edge cases        :   all negative numbers, single item, duplicate numbers, empty list, no valid pair
# Time Complexity   :   O(n)
# Space Complexity  :   O(1)
# Worst Case        :   O(n) consecutive numbers either at left or right.
# Best Case         :   O(1) numbers found at left and right ends.

class Solution:
    def twoSum(self, numbers:list[int], target:int)->list[int]:
        n = len(numbers)
        left, right = 0, (n-1)

        if n <= 1:
            return[]

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            if numbers[left] + numbers[right] > target:
                right = right-1
            else:
                left = left+1
        return []
if __name__ == '__main__':
    numbers = list(map(int, input("enter numbers").split(",")))
    target = int(input("enter target"))
    answer = Solution().twoSum(numbers, target)
    print(answer)