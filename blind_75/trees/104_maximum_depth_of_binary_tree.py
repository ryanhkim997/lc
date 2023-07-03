from typing import Optional
from collections import deque

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# using DFS, recursively
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # input: root node
        # output: maximum depth of tree as an int value
        # constraints:
            # The number of nodes in the tree is in the range [0, 104].
            # -100 <= Node.val <= 100
        # edge cases:
            # top node is null -> return zero
            
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# using BFS, iteratively
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        count = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            count += 1
        
        return count


# using DFS, iteratively
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        maxDepth = 0
        stack = [(root, 1)]
        while stack:
            curr, depth = stack.pop()
            maxDepth = max(maxDepth, depth)

            if curr.left:
                stack.append((curr.left, depth + 1))
            if curr.right:
                stack.append((curr.right, depth + 1))
        
        return maxDepth