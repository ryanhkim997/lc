from typing import List
from collections import deque

# using BFS, with queue
# O(n*m) time, where n is the number of rows and m is number of columns
# O(n*m) space, where the queue can potentially hold all values in the matrix
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        movement_list = [(1,0), (0,1), (-1,0), (0,-1)]
        seen = set()
        
        def traverse(i, j):
            q = deque([(i, j)])
            while q:
                curr_i, curr_j = q.popleft()
                if (curr_i, curr_j) not in seen:
                    seen.add((curr_i, curr_j))
                    for x, y in movement_list:
                        new_i, new_j = curr_i + x, curr_j + y
                        if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == "1":
                            q.append((new_i, new_j))
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in seen:
                    traverse(i, j)
                    count += 1

        return count

# using DFS and implicit stack in call stack
# O(n*m) time, where n is the number of rows and m is number of columns
# O(n*m) space, where stack can potentially hold all values in the matrix
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        count = 0

        def traverse(i, j):
            if not (0 <= i < rows) or not (0 <= j < cols) or grid[i][j] == "0":
                return

            if (i, j) not in seen:
                seen.add((i, j))
                traverse(i + 1, j)
                traverse(i - 1, j)
                traverse(i, j + 1)
                traverse(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in seen:
                    traverse(i, j)
                    count += 1
        
        return count