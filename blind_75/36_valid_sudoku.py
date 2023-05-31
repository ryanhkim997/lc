import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input: matrix 9x9 of strings that represent number inside of them or "." for no value
        # output: boolean representing whether board is valid or not
        # constraints: 
            # board.length == 9
            # board[i].length == 9
            # board[i][j] is a digit 1-9 or '.'.
        # edge cases:
            # period for blank spaces

        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True