# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def to_linked_list(head):
#     dummy = curr = ListNode()
#     for hd in head:
#         curr.next = ListNode(hd)
#         curr = curr.next
#     return dummy.next

# def to_list(l1):
#     result = []
#     while l1:
#         result.append(l1.val)
#         l1 = l1.next
#     return result

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if not head:
#             return None

#         dummy = ListNode(0)
#         dummy.next = head
#         first = dummy
#         second = dummy 

#         for i in range(n+1):
#             first = first.next

#         while first is not None:
#             first = first.next
#             second = second.next

#         second.next = second.next.next

#         return dummy.next

# if __name__ == '__main__':
#     head = list(map(int,input("enter linked list members = ").split(",")))
#     l1 = to_linked_list(head)
#     # print(to_list(l1))
#     result = Solution().removeNthFromEnd(l1, 3)
#     l2 = to_list(result)
#     print(l2)


# [4,5,6,7,8,9,10,0,1,2,3].   2
# [11,12,4,5,6,7,8,9,10].    12.       8

# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         left = 0
#         right = len(nums)-1

#         while left <= right:
#             mid = (left + right)//2

#             if nums[mid] == target:
#                 return mid

#             if nums[left] <= nums[mid]:
#                 if nums[left] <= target <= nums[mid]:
#                     right = mid -1
#                 else:
#                     left = mid + 1
#             else:
#                 if nums[mid] <= target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1
# if __name__ == '__main__':
#     nums = list(map(int,input("enter array members = ").split(",")))
#     target = int(input("enter target = "))
#     print(Solution().search(nums, target))

# Input: s = "abcabcbb"
# Output: 3

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#        char_set = set()
#        left = 0
#        max_len = 0

#        for right in range(len(s)):
#             while s[right] in char_set:
#                char_set.remove(s[left])
#                left = left + 1
#             char_set.add(s[right])
#             max_len = max(max_len , len(char_set))
       
#        return max_len

# Input: s = "BCBQABBB", k = 2
# Output: 4

# Input: s = "AABABBA", k = 1
# Output: 4
# AABABBA
# AAAA
# BBBB
    # def characterReplacement(self, s: str, k: int) -> int: 
    #     l = 0
    #     c_frequency = {}
    #     longest_str_len = 0
    #     for r in range(len(s)):
            
    #         if not s[r] in c_frequency:
    #             c_frequency[s[r]] = 0
    #         c_frequency[s[r]] += 1
            
    #         # Replacements cost = cells count between left and right - highest frequency
    #         cells_count = r - l + 1
    #         if cells_count - max(c_frequency.values()) <= k:
    #             longest_str_len = max(longest_str_len, cells_count)              
    #         else:
    #             c_frequency[s[l]] -= 1
    #             if not c_frequency[s[l]]:
    #                 c_frequency.pop(s[l])
    #             l += 1      
    #     return longest_str_len		      AABABBA
# def characterReplacement(self, s: str, k: int) -> int:
#     l = 0
#     longest_str_len = 0
#     c_frequency = {}

#     for r in range(len(s)):
#         if s[r] not in c_frequency:
#             c_frequency[s[r]] = 0
#         c_frequency[s[r]] = c_frequency[s[r]] + 1

#         cells_count = r - l + 1
#         if cells_count - max(c_frequency.values()) <= k:
#             longest_str_len = max(longest_str_len, cells_count)
#         else:
#             c_frequency[s[l]] = c_frequency[s[l]] - 1
#             if not c_frequency[s[l]]:
#                 c_frequency.pop(s[l])
#             l = l + 1
#     return longest_str_len

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         s_dict = {}
#         t_dict ={}

#         for i in range(len(s)):
#             s_dict[s[i]] = s_dict.get(s[i],0) + 1
#             t_dict[t[i]] = t_dict.get(t[i],0) + 1

#         if s_dict == t_dict:
#             return True 
        
#         return False


# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         if not strs:
#             return False
        
#         values_dict = {}

#         for s in strs:
#             value = "".join(sorted(s))

#             if value not in values_dict:
#                 values_dict[value] = []

#             values_dict[value].append(s)

#         return list(values_dict.values())

# class Solution:
#     def isValid(self, s: str) -> bool:
#         brackets_dict = {"(":")", "{":"}", "[":"]"}
#         stack = []

#         if len(s) % 2 != 0:
#             return False

#         for bracket in s:
#             if bracket in brackets_dict:
#                 stack.append(bracket)
#             else:
#                 if not stack or brackets_dict[stack.pop()] != bracket:
#                     return False
        
#         if len(stack) == 0:
#             return True
#         else:
#             return False


# class Solution:
#     def isPalindrome(self, s:str, p:int, q:int)->str:
#         while p >= 0 and q < len(s) and s[p] == s[q]:
#             p = p - 1
#             q = q + 1
#         return s[p+1 : q]

#     def longestPalindrome(self, s: str) -> str:
#         longest = ''
#         for i in range(len(s)):
#             odd_str = self.isPalindrome(s, i ,i)
#             even_str = self.isPalindrome(s, i, i+1)

#             longest = max(longest, odd_str, even_str, key = len)
#         return longest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution:
    def maxDepth(self, root:TreeNode)->int:
        if root is None:
            return 0

        maxLength = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return maxLength

if __name__ == "__main__":
    root = TreeNode(3, 
                    TreeNode(9), 
                    TreeNode(20, TreeNode(15), TreeNode(7, TreeNode(1), TreeNode(2))))
    print(Solution().maxDepth(root))






        
