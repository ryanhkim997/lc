from typing import List
from collections import deque

# solution technically works, but is too inefficient to pass leetcode tests. running bfs from each cell takes too long.
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        # seen = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(i, j):
            seen = set()
            q = deque([(i, j, 0)])

            while q:
                curr_i, curr_j, distance = q.popleft()
                if mat[curr_i][curr_j] == 0:
                    mat[i][j] = distance
                    return
                for x, y in directions:
                    if 0 <= curr_i + x < rows and 0 <= curr_j + y < cols and (curr_i + x, curr_j + y) not in seen:
                        seen.add((curr_i + x, curr_j + y))
                        q.append((curr_i + x, curr_j + y, distance + 1))
        
        for i in range(rows):
            for j in range(cols):
                bfs(i, j)
        
        return mat

# multi-source BFS solution; technically the same time and space complexity, but far less redundant
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        dist = [[-1 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        while q:
            i, j = q.popleft()

            for x, y in directions:
                ni, nj = i + x, j + y
                if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] == -1:
                    mat[ni][nj] = mat[i][j] + 1
                    q.append((ni, nj))

        return mat