# Medium
# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/

# Given a string s, return the number of palindromic substrings in it.
 
# Input: s = "abc"        Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Input: s = "aaa"        Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Edge cases        : 
# Time Complexity   : 
# Space complexity  :
# Best case         :                    
# Worst Case        : 

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res = res + 1
                left = left - 1
                right = right + 1
            return res

        for i in range(len(s)):
            count = count + expand(i, i)
            count = count + expand(i, i+1)
        return count
