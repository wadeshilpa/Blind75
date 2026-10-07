# Easy
# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:            Example 2:
#     3                     1
#    / \                     \
#   9  20                     2
#     /  \
#    15   7
# Output: 3             Output: 2

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def maxDepth(self, root:TreeNode)->int:
        if not root:
            return 0
        return (1 + max( self.maxDepth(root.left) ,  self.maxDepth(root.right)))
