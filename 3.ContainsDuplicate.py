# Easy
# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]               Output: true
# Input: nums = [1,2,3,4]               Output: false
# Input: nums = [1,1,1,3,3,4,3,2,4,2]   Output: true

# Edge Cases : empty, single element, negative numbers
# Time Complexity : O(n)
# Space COmplexity : O(n) ; usage of dictionary/set
# Best Case : consecutive duplicates at the start
# Worst Case : Duplicate is found at the end of the array. or duplicates do not exists.

class solution:
    def ContainsDuplicate(self,nums:list[int])->bool:
        nums_dict={}

        for i,num in enumerate(nums):
            if num in nums_dict:
                return True
            nums_dict[num]=1
        return False
    
    def ContainsDuplicate2(self,nums:list[int])->bool:
        seen=set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
if __name__=='__main__':
    try:
        nums=list(map(int,input("Enter nums array = ").split(",")))
        answer=solution().ContainsDuplicate(nums)
        print(answer)

        answer2=solution().ContainsDuplicate2(nums)
        print(answer2)
    except ValueError:
        print("Invalid input")
