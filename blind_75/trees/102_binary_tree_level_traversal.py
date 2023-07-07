from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # input: root of tree to traverse
        # output: list of node values, in order of level
        # constraints:
            # The number of nodes in the tree is in the range [0, 2000].
            # -1000 <= Node.val <= 1000
        # edge cases:
            # null root, only one tree node
            # uneven tree
        # notes:
            # most likely use bfs
            # binary tree, listing node values left to right

        output = []
        queue = deque([root])

        if not root:
            return []

        while queue:
            level_vals = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    level_vals.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            
            output.append(level_vals)
        
        return output