from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def dfs(s, left, right):
            if len(s) == 2 * n:
                output.append(s)
                return

            # if left is less than the number of pairs of parentheses
            if left < n:
                # recursive call to add left to list of strings, with left being incremented
                dfs(s + "(", left + 1, right)
            # if right is less than the number of left's
            if right < left:
                # recursive call to add right to list of strings, with right being incremented
                dfs(s+ ")", left, right + 1)
        
        dfs("", 0, 0)
        
        return output