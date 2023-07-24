from typing import List
from collections import deque

# bfs solution
# O(m * n) time potentially, usually better than that
# O(m * n) space, with the set keeping track of seen values
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # input: m x n matrix of ints, 3 ints 
        # output: modified matrix

        rows = len(image)
        cols = len(image[0])
        start_color = image[sr][sc]
        seen = set()

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(i, j):
            q = deque([(i, j)])

            while q:
                curr_i, curr_j = q.popleft()
                if (curr_i, curr_j) not in seen:
                    seen.add((curr_i, curr_j))
                    if image[curr_i][curr_j] == start_color:
                        image[curr_i][curr_j] = color
                        for x, y in directions:
                            if (0 <= curr_i + x < rows) and (0 <= curr_j + y < cols):
                                q.append((curr_i + x, curr_j + y))

        bfs(sr, sc)

        return image