from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # input: n x n matrix
        # output: modified matrix (in place)
        # constraints:
            # n == matrix.length == matrix[i].length
            # 1 <= n <= 20
            # -1000 <= matrix[i][j] <= 1000
        # edge cases:
            # 1x1 matrix
            # negative integers (shouldn't matter much since we aren't reading values)
            # matrix rows and columns are always the same
        
        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right

            for i in range(right - left):
                top_left = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = top_left
            
            left += 1
            right -= 1
        
        return matrix