from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # input: p and q, where each is the root of a binary tree
        # output: boolean indicating whether they are the same or not (true if same, false if not)
        # constraints:
            # The number of nodes in both trees is in the range [0, 100].
            # -104 <= Node.val <= 104
        # edge cases:
            # can be empty tree
        
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))