from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output: tuple indicating two indices adding up to target
        # input: list to search, target sum
        # constraints: 
            # 2 <= nums.length <= 104
            # -109 <= nums[i] <= 109
            # -109 <= target <= 109
            # Only one valid answer exists.
        # edge cases:
            # negative ints?

        # # iterate through list (i)
        #     for i in range(len(nums)):
        #     # iterate through list (j)
        #         for j in range(len(nums)):
        #         # if list[i] + list[j] == target
        #             if nums[i] + nums[j] == target and i != j:
        #                 # return [i, j]
        #                 return [i, j]

        # set pointer to 0
        tracker = {}

        for i, j in enumerate(nums):
            if target - j in tracker:
                return [i, tracker[target - j]]

            tracker[j] = i