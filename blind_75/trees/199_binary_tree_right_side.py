from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # input: root of binary tree
        # output: list of integers representing values of right side nodes only
        # constraints:
            # The number of nodes in the tree is in the range [0, 100].
            # -100 <= Node.val <= 100
        # edge cases:
            # empty root: return empty list
        output = []
        queue = deque([root])

        while queue:
            stop_point = len(queue) - 1
            for i in range(len(queue)):
                curr = queue.popleft()

                if i == stop_point and curr:
                    output.append(curr.val)
                
                if curr and curr.left:
                    queue.append(curr.left)
                if curr and curr.right:
                    queue.append(curr.right)
        
        return output