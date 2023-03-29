from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # output: all possible subsets, including empty array
        # input: list of unique elements (all integers)
        # constraints:
            # 1 <= nums.length <= 10
            # -10 <= nums[i] <= 10
            # All the numbers of nums are unique.
            # no dupes, any order is fine
        # edge cases:
            # empty array is considered a subset
        output = []
        def backtrack(subarr, idx):
            output.append(subarr)
            if len(subarr) == len(nums):
                return
            
            for i in range(idx, len(nums)):
                idx += 1
                backtrack(subarr + [nums[i]], idx)

        
        backtrack([], 0)
        return output