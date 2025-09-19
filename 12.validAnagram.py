# Easy
# Valid Anagram
# Hash Map / Dictionary

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# using all the original letters exactly once.
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# s and t consist of lowercase English letters.

# Input: s = "anagram", t = "nagaram"         Output: true
# Input: s = "rat", t = "car"                 Output: false

# Edge cases        : unequal lengths, different cases, one empty string, duplicate characters
# Time Complexity   : O(n)
# Space complexity  : O(1) if character set is fixed (e.g., lowercase English letters, max 26 keys), otherwise O(n) for arbitrary characters.
# Best case         : When len(s) != len(t) → returns False immediately in O(1) time.
# Worst Case        : Strings are the same length → builds both dictionaries and compares them → O(n) time.
########################################################################
class Solution:
    def validAnagram(self, s:str, t:str)-> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}
        
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1

        if dict_s == dict_t:
            return True 
        
        return False

if __name__ == "__main__":
    s = input("Enter s string = ")
    t = input("Enter t string = ")
    print(Solution().validAnagram(s,t))
