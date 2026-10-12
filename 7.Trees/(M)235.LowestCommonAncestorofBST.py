# Medium 
# Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
# two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

# Example 1:                 Example 2:                 Example 3:
#         6                          6                          2
#        / \                        / \                        /
#       2   8                      2   8                      1
#      / \ / \                    / \ / \
#     0  4 7  9                  0  4 7  9
#       / \                        / \
#      3   5                      3   5

# p = 2, q = 8               p = 2, q = 4               p = 1, q = 2
# Output: 6                  Output: 2                  Output: 2

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
