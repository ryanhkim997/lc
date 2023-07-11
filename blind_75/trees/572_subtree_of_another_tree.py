from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # input: root of tree, subRoot of potential sub tree
        # output: boolean representing whether subroot is a sub tree of root tree
        # constraints:
            # The number of nodes in the root tree is in the range [1, 2000].
            # The number of nodes in the subRoot tree is in the range [1, 1000].
            # -104 <= root.val <= 104
            # -104 <= subRoot.val <= 104
        # edge cases:
            # subroot is the same as root
        def isSameTree(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            return (isSameTree(n1.left, n2.left) and isSameTree(n1.right, n2.right))

        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))