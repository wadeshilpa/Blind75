# Easy
# Maximum Depth of Binary Tree   
# recursive Depth-First Search (DFS)

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]           Output: 3
# Input: root = [1,null,2]                        Output: 2

#     maxDepth = 1 + max(maxDepth(9), maxDepth(20))
#     maxDepth = 1 + max(1+ max(maxDepth(None),tre(None), 1+ max(maxDepth(15), maxDepth(7))
#     maxDepth = 1 + max(1+ 0, 1+ max(maxDepth(15), maxDepth(7))
#     maxDepth = 1 + max(1+ 0, 1+ max(1 + 0, 1 + 0)    
#     maxDepth = 1 + max(1, 1+ 1)               
#     maxDepth = 3

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right

class Solution:
    def maxDepth(self, root:TreeNode)->int:
        if root == None:
            return 0
        
        maxDepth = 1+ (max(self.maxDepth(root.left), self.maxDepth(root.right)))
        return maxDepth


if __name__ == "__main__":
    root = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().maxDepth(root))
    
