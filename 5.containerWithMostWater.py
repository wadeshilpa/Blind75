# Difficulty : Medium
# Container With Most Water
# Two Pointer

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# height = [1,1]                        Output: 1
# height = [5,5,5,5]                    Output: 15
# height = [1,2,3,4,5]                  Output: 6
# height = [1,8,6,2,5,4,8,3,7]          Output: 49
# The two tallest optimal lines here are at index 1 (height 8) and index 8 (height 7).

# 8 |   |         |    
# 7 |   |         |   |
# 6 |   | |       |   |
# 5 |   | |   |   |   |
# 4 |   | |   | | |   |
# 3 |   | |   | | | | |
# 2 |   | | | | | | | |
# 1 | | | | | | | | | |
# 0 +-------------------
#     0 1 2 3 4 5 6 7 8

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def maxArea(self, height:list[int])->int:
        left = 0
        right = len(height)-1
        maxarea = 0

        while left < right:
            x = height[left]
            y = height[right]

            area = (right - left) * min(x,y)
            maxarea = max(area, maxarea)

            if x < y:
                left = left + 1
            else:
                right = right - 1
        return maxarea

if __name__ == '__main__':
    height = list(map(int,input("Enter height array = ").split(",")))
    print(Solution().maxArea(height))

