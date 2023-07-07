from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            maxSum[0] = max(maxSum[0], maxLeft + maxRight + root.val)

            return max(maxLeft + root.val, maxRight + root.val)

        dfs(root)
        return maxSum[0]