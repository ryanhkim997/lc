from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque([node])
        clone = Node(node.val)
        visited = {}
        visited[node] = clone

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    clone_neighbor = Node(neighbor.val)
                    visited[neighbor] = clone_neighbor
                    visited[curr].neighbors.append(clone_neighbor)
                    q.append(neighbor)
                else:
                    visited[curr].neighbors.append(visited[neighbor])

        return clone