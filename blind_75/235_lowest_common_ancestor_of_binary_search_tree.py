# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # input: root node, p node, q node (BST)
        # output: lowest node in BST where p and q are descendents of it
        # constraints:
            # The number of nodes in the tree is in the range [2, 105].
            # -109 <= Node.val <= 109
            # All Node.val are unique.
            # p != q
            # p and q will exist in the BST.
        # edge cases:
            # p and q never equal, values are all unique
            # two nodes are both p and q
        
        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val) or root.val == p.val or root.val == q.val:
            return root
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
# optimized/simplified
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # input: root node, p node, q node (BST)
        # output: lowest node in BST where p and q are descendents of it
        # constraints:
            # The number of nodes in the tree is in the range [2, 105].
            # -109 <= Node.val <= 109
            # All Node.val are unique.
            # p != q
            # p and q will exist in the BST.
        # edge cases:
            # p and q never equal, values are all unique
            # two nodes are both p and q
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root