# Medium
# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums:list[int],k:int)->list[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        frequency = dict(sorted(frequency.items(), key = lambda x:x[1], reverse = True))

        return list(frequency.keys())[:k]
