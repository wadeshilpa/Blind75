# Medium
# Combination Sum
# https://leetcode.com/problems/combination-sum/description/

# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Input: candidates = [2,3,6,7], target = 7   Output: [[2,2,3],[7]]
# Input: candidates = [2,3,5], target = 8     Output: [[2,2,2,2],[2,3,3],[3,5]]
# Input: candidates = [2], target = 1         Output: []

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path + [nums[i]], res)

