from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()
        fresh = 0
        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while rotten:
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for x, y in directions:
                    ni, nj = i + x, j + y
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        rotten.append((ni, nj))
                        fresh -= 1
            if rotten:
                minutes += 1
        
        if fresh > 0:
            return -1
        else:
            return minutes