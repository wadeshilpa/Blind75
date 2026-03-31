# Difficulty : Medium
# Longest Consecutive Sequence
# Hash Set Lookup
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]        Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Input: nums = [0,3,7,2,5,8,4,6,0,1]   Output: 9

# Input: nums = [1,0,1,2].              Output: 3

# Edge cases        : Empty, all negative, positive + negative, duplicates, all duplicates, sorted, shuffled
# Time Complexity   : O(n) 
# Space complexity  : O(n) - For the set
# Best case         : O(n) no consecutive neighbors. While is executed only once per number. [10, 30, 50, 70]
# Worst Case        : All numbers form a single long consecutive sequence..
#                     The smallest number (1) triggers the while loop, but that loop iterates through all n numbers once
########################################################################
class solution:
    def longestSequence(self, nums:list[int])->int:
        if not nums:
            return 0
            
        max_count = 0
        num_set = set(nums) 

        for num in num_set:                          #  iterate set to skip duplicates
            counter = 0
            if (num - 1) not in num_set:
                while num  in num_set:
                    num = num + 1
                    counter = counter + 1
                max_count = max(max_count, counter)
        return max_count

if __name__ == '__main__':
    nums = list(map(int,input("enter an integer arrray = ").split(",")))
    print(solution().longestSequence(nums))
