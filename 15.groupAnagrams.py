# Medium
# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]       Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Input: strs = [""]        Output: [[""]]
# Input: strs = ["a"]       Output: [["a"]]

# Edge cases        : Blank, all anagrams, single string, duplicates, numbers
# Time Complexity   : O(n * k log k)  # n = number of strings, k = max string length. Sorting each string costs O(k log k)
# Space complexity  : O(n * k)  # to store all strings in the hashmap. Plus O(k) for temporary sorted string (per iteration).   
# Best case         : 
# Worst Case        : 
########################################################################
# from collections import defaultdict
class Solution:
    def groupAnagram(self, strs:list[str])->list[list[str]]:
        if not strs:
            return []
        map_groups = {}
        # map_groups = defaultdict(list)        can use this to avoid line 27 & 28. don’t have to manually check if a key exists before appending.
        
        for s in strs:
            key = "".join(sorted(s))
            if not key in map_groups:
                map_groups[key] = []
            map_groups[key].append(s)

        return list(map_groups.values())
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagram(strs))
    strs = ["a"]
    print(Solution().groupAnagram(strs))
    strs = [""]
    print(Solution().groupAnagram(strs))


