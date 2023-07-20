from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # input: root of bst, int k
        # output: kth smallest value as integer of all nodes in bst
        # constraints:
            # The number of nodes in the tree is n.
            # 1 <= k <= n <= 104
            # 0 <= Node.val <= 104
        # edge cases:
            # no negative vals
            # number of nodes always at least one, and k is always less than or eq to number of nodes in tree
        
        # traverse tree only on left side => returns smallest value
        # if we pop that value and do the left side traversal k times, we have n * log(n) time
        res = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res[k - 1]
    
# notes:
    # inorder traversal of BST always yields elements in order