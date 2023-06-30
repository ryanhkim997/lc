from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                maxArea = max(maxArea, height * (i - index))

            stack.append((start, h))
        
        for i in stack:
            index, height = i
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea