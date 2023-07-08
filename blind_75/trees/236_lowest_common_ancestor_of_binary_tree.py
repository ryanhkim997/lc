# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # input: root of tree, p value of tree node, q value of node to find LCA of
        # output: LCA of p and q nodes
        # constraints:
            # The number of nodes in the tree is in the range [2, 105].
            # -109 <= Node.val <= 109
            # All Node.val are unique.
            # p != q
            # p and q will exist in the tree.
        # edge cases:
            # always at least two nodes
        # notes:
            # if p == root or q == root:
                # return root
            # 
        if not root or root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None