# Difficulty : Medium
# Longest Substring Without Repeating Characters
# Sliding Window

# Given a string s, find the length of the longest substring without duplicate characters.

# Input: s = "abcabcbb"           Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"              Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"             Output: 3
# Explanation: "wke", length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
########################################################################
# class solution:
#     def lengthOfLongestSubstring(self, s:str)->int:
#         max_length = 0
#         for i in range(len(s)):
#             s_set = set()
#             length = 0
#             while (i + length) < len(s) and s[i + length] not in s_set:
#                 s_set.add(s[i + length])
#                 length = length + 1
#             max_length= max(length, max_length)
#         return max_length
 
# if __name__ == "__main__":
#     s = input("Enter the string = ")
#     print(solution().lengthOfLongestSubstring(s))
########################################################################
class solution:
    def lengthOfLongestSubstring(self, s:str)->int:
        left = 0
        max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left = left + 1

            char_set.add(s[right])
            max_length = max(max_length, (right - left + 1))
        return max_length
 
if __name__ == "__main__":
    s = input("Enter the string = ")
    print(solution().lengthOfLongestSubstring(s))

