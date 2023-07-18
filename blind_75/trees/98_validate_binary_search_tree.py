from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float("-inf"), max_val=float("inf")) -> bool:
        # input: root of binary tree
        # output: boolean indicating if bst => true, if not false
        # constraints:
            # The number of nodes in the tree is in the range [1, 104].
            # -231 <= Node.val <= 231 - 1
        # edge cases:
            # only one node
        
        if not root:
            return True
        
        if not min_val < root.val < max_val:
            return False
        
        return (self.isValidBST(root.left, min_val, root.val) and self.isValidBST(root.right, root.val, max_val))