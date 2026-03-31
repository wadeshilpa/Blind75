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


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 

# class Solution:
#     def maxDepth(self, root:TreeNode)->int:
#         if root is None:
#             return 0

#         maxLength = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#         return maxLength

# if __name__ == "__main__":
#     root = TreeNode(3, 
#                     TreeNode(9), 
#                     TreeNode(20, TreeNode(15), TreeNode(7, TreeNode(1), TreeNode(2))))
#     print(Solution().maxDepth(root))

# You are given two integer arrays departures[0..n-1] and returns[0..n-1], 
# where departures[i] is the ticket cost to depart on day i and 
#     returns[j] is the ticket cost to return on day j.
# Choose a pair of days (i, j) such that 0 ≤ i < j < n (return must be on a later day) 
# to minimize the total cost departures[i] + returns[j].

# Example: departures=[1,2,3,4], returns=[4,3,2,1] → minimum cost 2 (depart day 0, return day 3).


# if __name__ == "__main__":
#     print("hi")

#     # departures=[1,2,3,4]
#     # returns=[4,3,2,1] 
#     departures=[1,2,3,4]
#     returns=[4,3,2,5,6,2,1] 

#     min_departures = departures[0]
#     min_price = float("inf")

#     # for i in range(len(departures)):
#     #     departure = departures[i]
#     #     if departure < min_departures:
#     #         min_departures = departure

#     #     min_price = min(min_price, (returns[i]+min_departures))

#     # for i in range(i, len(returns)):
#     #     min_price = min(min_price, (returns[i]+min_departures))

#     # print(min_price)    

#     for j in range(1, len(returns)):
#         if j < len(departures):
#             if departures[j-1] < min_departures:
#                 min_departures = departures[j]

#         min_price = min(min_price, (returns[j] + min_departures))

#     print(min_price)


        


class solution:
    def containsDuplicate(self, nums:list[int])->bool:
        if not nums or len(nums) < 2:
            return False
        
        seen = set()

        for num in nums:
            if num in seen:
                return True 
            seen.add(num)

        return False
    
Input: s = "racecar", t = "carrace"

Output: true

class solution:
    def validAnagram(self, s:str, t:str)->bool:
        if len(s) != len(t):
            return False
        
        if not s:
            return True 
        
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        if s_dict == t_dict:
            return True 
        
        return False
    

class solution:
    def twoSum(self, nums:list[int], target:int)->list[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in nums_dict:
                return [nums_dict[diff], i]
            
            nums_dict[num] = i

        return []
    


class solution:
    def groupAnagrams(self, strs:list[str])->list[list[str]]:
        map_groups = {}
        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s not in map_groups:
                map_groups[sorted_s] = []

            map_groups[sorted_s].append(s)

        return list(map_groups.values())
    

nums = [1,2,2,3,3,3], k = 2.    Output: [2,3]
nums = [7,7], k = 1             Output: [7]

class solution:
    def topKFrequent(self, nums:list[int],k:int)->list[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        frequency = dict(sorted(frequency.items(), key = lambda x:x[1], reverse = True))

        return list(frequency.keys())[:k]





Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]


class Solution:
    def productExceptItself(self, nums:list[int])->list[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        product = [1] * n

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(len(nums)):
            product[i] = left[i] * right[i]

        return product
    

class Solution:
    def containsDuplicate(self, nums:list[int])->bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True 
            num_set.add(num)

        return False
        
class Solution:
    def validAnagram(self, s:str, t:str)->bool:
        if len(s) != len(t):
            return False 
        
        if not s:
            return True
        
        s_dict = {}
        t_dict = {}
        
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return s_dict == t_dict

class Solution:
    def twoSum(self, nums:list[int], target:int)->list[int]:
        if not nums:
            return [] 
        
        num_dict = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in num_dict:
                return [num_dict[diff], i]
            
            num_dict[num] = i 

        return []
        
class Solution:
    def groupAnagram(self, strs:list[str])->list[list[str]]:
        if not strs:
            return []

        s_dict = {}

        for s in strs:
            s_sorted = "".join(sorted(s))

            if s_sorted not in s_dict:
                s_dict[s_sorted] = []

            s_dict[s_sorted].append(s)

        return list(s_dict.values())


class Solution:
    def buyAndSellStock(self, prices:list[int])->int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price 
            
            profit = price - min_price
            max_profit = max(profit, max_profit)

        return max_profit
    
 [1, 8, 6, 2, 5, 4, 8, 3, 7]. Output: 49

class Solution:
    def containerWithMostWater(self, height:list[int])->int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            maxArea = max(area, maxArea)

            if height[left] < height[right]:
                left = left + 1 
            else:
                right = right - 1

        return maxArea
    

Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1

class Solution:
    def findInRotatedSortedArray(self, nums:list[int], target:int)->int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid 
            
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        


Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6

Input:  nums = [1]
Output: 1

Input:  nums = [5, 4, -1, 7, 8]
Output: 23

class Solution:
    def maxSubarray(self, nums:list[int])->int:
        num_set = set(nums)
        max_counter = 0

        for num in num_set:
            counter = 0
            if (num-1) not in num_set:
                while num in num_set:
                    num = num + 1
                    counter = counter + 1
                max_counter = max(counter, max_counter)
        return max_counter
                

class Solution:
    def maxSubarraySum(self, nums:list[int])->int: 
        current_sum = nums[0]
        max_current_sum = nums[0]

        for num in nums[1:]:
            if (current_sum + num) <= num:
                current_sum = num
            else:
                current_sum = current_sum + num
            max_current_sum = max(current_sum, max_current_sum)

        return max_current_sum

Input:  nums = [3, 4, 5, 1, 2]
Output: 1
Explanation: Original array was [1,2,3,4,5], rotated 3 times

Input:  nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0

Input:  nums = [4, 5, 6, 7, 8, 9, 0, 1, 2]
Output: 0

[14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12, 13]

class Solution:
    def minInRotatedSortedArray(self, nums:list[int])->int:
        left = 0
        right = len(nums)-1

        if nums[left] < nums[right]:
            return nums[left]
        
        while left <= right:
            mid = (left + right)//2

            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid 


Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1, 2]

Input:  nums = [1], k = 1
Output: [1]


class Solution:
    def topKFrequent(self, nums:list[int], k:int)->list[int]:
        n_dict = {}

        for n in nums:
            n_dict[n] = n_dict.get(n, 0) + 1

        n_dict = dict(sorted(n_dict.items(), key = lambda x:x[1], reverse=True))

        return list(n_dict.keys())[:k]




