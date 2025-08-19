# Difficulty : Medium
# Longest Palindromic Substring
# Expand from center

# Given a string s, return the longest palindromic substring in s.
# palindrome = A string is palindromic if it reads the same forward and backward.

# Input: s = "babad"      Output: "bab" OR "aba"
# Input: s = "cbbd"       Output: "bb"
# Input: s = "forgeeksskeegfor"     Output: "geeksskeeg"
# Input: s = "aaaa"       Output: "aaaa"

# Edge cases        : case sensitive, empty, single, even-odd length
# Time Complexity   : O(n²)
# Space complexity  : O(1) auxiliary, O(k) temporary per expansion result(k = palindrome length)
# Best case         : The best case happens when expansions end quickly for each center, 
#                     e.g., all characters are different like "abcdef".
#                     Each center check stops after 1 comparison → O(n) total time.
# Worst Case        : Happens when the string is highly repetitive, e.g., "aaaaaa", or full palindrome.
#                     Each center expansion can go nearly n steps → O(n²) total time.
########################################################################

class Solution():
    def longestPalindrome(self, s:str)->str:  # O(n³) - for, for, reverse
        if not s:
            return ""
        longest = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word == word[::-1]:
                    longest = max(longest, word, key = len)
        return longest
    
    def longestPalindrome2(self, s:str)->str:  #O(n²)
        if len(s) <= 1:
            return s
        longest = s[0]
        def expand_from_center(left, right)->str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left = left - 1
                right = right + 1
            return s[left+1:right]
        
        for i in range(0,len(s)):
            odd = expand_from_center(i,i)
            even = expand_from_center(i,i+1)

            longest = max(odd, even, longest, key = len)
        return longest

if __name__ == '__main__':
    s = input("Enter string s = ")
    print(Solution().longestPalindrome(s))
    print(Solution().longestPalindrome2(s))



