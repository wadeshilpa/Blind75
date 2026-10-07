# Easy 
# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:                 Example 2:                 Example 3:                 Example 4:
# root =    3                root =    3                root =    1                root =    1
#          / \                        / \                        / \                        / \
#         4   5                      4   5                      1   1                      2   3
#        / \                        / \                                                 /
#       1   2                      1   2                                                4
#                                    /
#                                   0

# subRoot = 4               subRoot = 4               subRoot = 1               subRoot = 2
#          / \                       / \                                             /
#         1   2                     1   2                                           4

# Output: true              Output: false             Output: true              Output: false

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True
        
        if root is None:
            return False
        
        def isSameTree(p:TreeNode, q:TreeNode)->bool:
            if p is None and q is None:
                return True 
            
            if p is None or q is None:
                return False 
            
            if p.val != q.val:
                return False 
            
            return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))
        
        return (isSameTree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot)
                )