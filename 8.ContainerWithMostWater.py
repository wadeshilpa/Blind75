# Difficulty : medium 

# Given an integer array;
# find two vertical lines such that together they form a container that holds the maximum amount of water. 
# The container cannot be slanted. 
# Return the maximum amount of water the container can store.

# Input: height = [1,8,6,2,5,4,8,3,7]    Output: 49
# Input: height = [1,1]                  Output: 1

# Edge cases : 
# Time Complexity : O(n); The two-pointer technique ensures that each element is processed at most once.
# Space Complexity :  O(1); constant amount of extra space regardless of the input size
# Worst Case : O(n)
# Best Case : O(n); Even in the best case, the two-pointer technique must check each pair of lines

# Brute force - O(N^2)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         area = 0
#         for i in range(len(height)):
#             x = height[i]

#             for j in range(i+1,len(height)):
#                 y = height[j]

#                 area = max(area, min(x,y) * (j-i))
#         return area

class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        left = 0
        right = len(height)-1

        while left < right:
            x = height[left]
            y = height[right]

            area = max(area, min(x,y)*(right-left) )

            if x <= y:
                left = left+1
            else:
                right = right -1
        return area
if __name__ == '__main__':
    height = list(map(int,input("enter heights").split(",")))
    answer = Solution().maxArea(height)
    print(answer)

