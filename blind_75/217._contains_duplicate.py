from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # output: boolean indicating whether every element is distinct or not
        # input: array of nums
        # constraints:
            # 1 <= nums.length <= 105
            # -109 <= nums[i] <= 109
        # edge cases:
            # 
        
        tracker = {}

        for val in nums:
            if val in tracker:
                return True

            tracker[val] = True
        
        return False