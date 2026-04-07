# Medium 
# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous non-empty sequence of characters within a string.

# Input: s = "abcabcbb"       Output: 3
# Input: s = "bbbbb"          Output: 1
# Input: s = "pwwkew"         Output: 3

# Edge cases        : empty, single char, special characters, duplicate chars
# Time Complexity   : O(n)
# Space complexity  : O(n)
# Best case         : O(n)
# Worst Case        : O(n)  each character is added and removed at most once
########################################################################
class Solution:
    def lengthOfLongestSubstring(self, s:str)->int:
        if not s:
            return 0
        
        charSet = set()
        left = 0
        maxLength = 0

        for right in s:
            while right in charSet:
                charSet.remove(s[left])
                left +=  1
            charSet.add(right)
            maxLength = max(len(charSet), maxLength)

        return maxLength