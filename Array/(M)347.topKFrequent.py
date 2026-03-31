# Medium
# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

# Given an integer array nums and an integer k,
# return the k most frequent elements.
# You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2         Output: [1, 2]
########################################################################

class Solution:
    def topKFrequent(self, nums:list[int],k:int)->list[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        frequency = dict(sorted(frequency.items(), key = lambda x:x[1], reverse = True))

        return list(frequency.keys())[:k]
