# Easy
# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/

# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:            Example 2:            Example 3:
#     4                     2                     1
#    / \                   / \                   /
#   2   7                 1   3                 2
#  / \ / \                                     /
# 1  3 6  9                                   3

#     4                     2                   1
#    / \                   / \                   \
#   7   2                 3   1                   2
#  / \ / \                                         \
# 9  6 3  1                                         3

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class TreeNode:
    def __init__(self, val:int=0, left:TreeNode=None, right:TreeNode=None):
        self.val = val
        self.left = left 
        self.right = right
class Solution:
    def invertTree(self, root:TreeNode)->TreeNode:
        if root is None:
            return None 
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root