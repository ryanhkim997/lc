from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(heights)
        cols = len(heights[0])
        p_seen = set()
        a_seen = set()
        p_q = deque()
        a_q = deque()
        output = []

        def bfs(ocean_q, ocean_seen):
            while ocean_q:
                i, j = ocean_q.popleft()
                for x, y in directions:
                    ni, nj = i + x, j + y
                    if (0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in ocean_seen and heights[ni][nj] >= heights[i][j]):
                        ocean_q.append((ni, nj))
                        ocean_seen.add((ni, nj))

        for r in range(rows):
            p_seen.add((r, 0))
            p_q.append((r, 0))

        for c in range(cols):
            p_seen.add((0, c))
            p_q.append((0, c))
        
        bfs(p_q, p_seen)

        for r in range(rows):
            a_seen.add((r, cols - 1))
            a_q.append((r, cols - 1))

        for c in range(cols):
            a_seen.add((rows -1, c))
            a_q.append((rows - 1, c))
        
        bfs(a_q, a_seen)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in a_seen and (r, c) in p_seen:
                    output.append([r, c])


        return output