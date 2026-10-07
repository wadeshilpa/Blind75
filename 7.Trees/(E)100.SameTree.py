# Easy
# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:            Example 2:            Example 3:            Example 4:
# p =   1               p =   1               p =   1               p = empty
#      / \                   /                     / \               q = empty
#     2   3                 2                     2   1             Output: true

# q =   1               q =   1               q =   1
#      / \                     \                   / \
#     2   3                     2                 1   2

# Output: true          Output: false         Output: false

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def isSameTree(self, p:TreeNode, q:TreeNode)->bool:
        if p is None and q is None:
            return True 
        
        if p is None or q is None:
            return False 
        
        if p.val != q.val:
            return False 
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))