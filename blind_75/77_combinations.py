from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # output: list of lists, where each list is a distinct combination of len k in the range 1 - n
        # input: int n (range of combo) and int k (length of combo)
        # constraints:
            # 1 <= n <= 20
            # 1 <= k <= n
        # edge cases:
            # 
        
        # keep track of number of numbers in a particular combination
        output = []

        # m: current number to find combos from
        def dfs(m, combo):
            # base case: append to output string
            if len(combo) == k:
                output.append(combo)
                return

            for i in range(m, n + 1):
                m += 1
                dfs(m, combo + [i])


        dfs(1, [])
        return output