# Medium
# Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Input: s = "ABAB", k = 2        Output: 4
# Input: s = "AABABBA", k = 1     Output: 4

# Edge cases        : empty, special chars, repeating chars
# Time Complexity   : O(n)
# Space complexity  : O(1) The charSet dict holds at most 26 uppercase English letters — it's bounded, not proportional to input size.
# Best case         : O(n)
# Worst Case        : O(n)
########################################################################
class Solution:
    def characterReplacement(self, s:str, k:int)->int:
        if not s:
            return 0
        
        charSet = {}
        left = 0
        maxLength = 0

        for right, char in enumerate(s):
            charSet[char] = charSet.get(char, 0) + 1

            if (((right-left+1) - max(charSet.values())) > k):
                charSet[s[left]] = charSet.get(s[left], 0) - 1
                left +=  1
            
            maxLength = max((right-left+1), maxLength)

        return maxLength
