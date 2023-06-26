from typing import List

# O(n) time, O(n) space solution
class Solution:
    def trap(self, height: List[int]) -> int:
        # input: list of non-negative integers representing elevation map
        # output: integer representing how much water the list can trap after raining
        # constraints:
            # n == height.length
            # 1 <= n <= 2 * 10^4
            # 0 <= height[i] <= 105
        # edge cases:
            # height must be of length 1 or more
                # if height is 1 then no rain water can be trapped

        maxL = [0] * len(height)
        curr_maxL = 0
        maxR = [0] * len(height)
        curr_maxR = 0
        minLandR = []
        total = 0

        for i in range(len(height)):
            if not maxL or curr_maxL < height[i]:
                maxL[i] = curr_maxL
                curr_maxL = height[i]
            else:
                maxL[i] = curr_maxL
        
        for i in range(len(height) - 1, -1, -1):
            if not maxR or curr_maxR < height[i]:
                maxR[i] = curr_maxR
                curr_maxR = height[i]
            else:
                maxR[i] = curr_maxR
        
        for i in range(len(height)):
            minLandR.append(min(maxR[i], maxL[i]))

        for i in range(len(height)):
            if minLandR[i] - height[i] > 0:
                total = total + minLandR[i] - height[i]
        
        return total

# O(n) time, O(1) space solution
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]
        total = 0

        if not height: return 0

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(height[left], maxL)
                if maxL - height[left] > 0:
                    total += maxL - height[left]
            else:
                right -= 1
                maxR = max(height[right], maxR)
                if maxR - height[right] > 0:
                    total += maxR - height[right]
                

        return total
