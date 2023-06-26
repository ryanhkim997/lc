from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # input: array of int's, temperatures
        # output: array such that answer[i] is the number of days you have to wait after ith day to get a warmer temp
        # constraints:
            # 1 <= temperatures.length <= 10^5
            # 30 <= temperatures[i] <= 100
        # edge cases:
            # only one temp => 0
        
        stack = []
        output = [0] * len(temperatures)
        i = 0
        while i < len(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                output[stack[-1][1]] = (i - stack[-1][1])
                stack.pop()
            stack.append([temperatures[i], i])
            i += 1
        
        return output

# notes:
    # tricky part is using monotonic decreasing stack with a tuple containing both temperature and index of the temperature
    # output has to be initialized to len(temperatures) values
    # roughly O(n) time, but it'll take a little longer than that since we're backtracking a bit while going through temperatures list