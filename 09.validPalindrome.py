# Easy
# Valid Palindrome
# Two pointer

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"         Output: true
#         Explanation: "amanaplanacanalpanama" is a palindrome.
# Input: s = "race a car"                             Output: false
# Input: s = " "                                      Output: true
# Input s = "No lemon, no melon"                      Output: true
# Input s = "123421"                                  Output: fasle
# Input s = "12321"                                   Output: true

# Edge cases        : empty, sigle, all numeric, only special characters
# Time Complexity   : O(n)
# Space complexity  : O(1)
# Best case         : O(1) - Early mismatch after minimal skipping
# Worst Case        : (n) - Full pass with all pairs matching
########################################################################
class Solution:
    def validPalindrome(self,s:str)->bool:     # space = O(n)
        word = []
        for i in range(len(s)):
            if s[i].isalnum():
                word.append(s[i].lower())
        return word == word[::-1]
    
    def validPalindrome2(self,s:str)->bool:     # space = O(1)
        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left = left + 1
                continue
            if not s[right].isalnum():
                right = right - 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            left = left + 1
            right = right - 1

        return True

if __name__ == '__main__':
    s = input("enter string s = ")
    print(Solution().validPalindrome(s))
    print(Solution().validPalindrome2(s))