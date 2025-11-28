# Easy
# Same Tree
# Recursive Depth-First Search (DFS)

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]         Output: true
# Input: p = [1,2], q = [1,null,2]        Output: false
# Input: p = [1,2,1], q = [1,1,2]         Output: false

# Edge cases        : empty both or either, negative values, same structure diff values
# Time complexity   : O(n) where n is the total number of nodes in the smaller tree
# Space complexity  : O(h) — where h is the height of the tree.
                        # This is the recursion call stack depth:
                        # Best case (balanced tree): O(log n)
                        # Worst case (skewed tree): O(n)
# Best case         : When both roots are None → returns immediately (O(1) time, O(1) space).
# Worst case        : Two large identical or completely mismatched trees → need to traverse all nodes.
########################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def isSameTree(self, p:TreeNode, q: TreeNode)->bool:
        if not p and not q:
            return True 
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

if __name__ == '__main__':
    # ✅ Test Case 1: Identical Trees
    p = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7)))
    q = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7)))
    
    print(Solution().isSameTree(p, q))

    # ✅ Test Case 2: Value mismatch
    p = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7)))
    q = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(8)))
    
    print(Solution().isSameTree(p, q))

    # ✅ Test Case 3: Both empty
    p = None
    q = None
    print(Solution().isSameTree(p, q))
