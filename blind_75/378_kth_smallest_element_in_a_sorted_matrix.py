from bisect import bisect_right
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # input: n x n matrix where rows and columns sorted in asc order, k, where k is the kth smallest element to find
        # output: kth smallest element
        # constraints:
            # n == matrix.length == matrix[i].length
            # 1 <= n <= 300
            # -109 <= matrix[i][j] <= 109
            # All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
            # 1 <= k <= n^2
        # edge cases:
            # 1x1 matrix
            # k is 1 or n^2
        
        # two pointers, essentially binary search


        # while left < right:

        # brute force
        
        # flattened_list = []

        # for i in matrix:
        #     flattened_list.extend(i)
        
        # flattened_list.sort()
        
        # return flattened_list[k - 1]

        left, right, size = matrix[0][0], matrix[-1][-1], len(matrix)

        def el_less_k(mp):
            count = 0

            for r in range(size):
                x = bisect_right(matrix[r], mp)
                count += x

            return count

        while left < right:
            mid = (left + right) // 2

            if el_less_k(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left