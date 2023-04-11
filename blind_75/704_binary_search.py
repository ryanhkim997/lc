from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # output: index of target
        # input: list of sorted nums in ascending order
        # constraints:
            # 1 <= nums.length <= 104
            # -104 < nums[i], target < 104
            # All the integers in nums are unique.
            # nums is sorted in ascending order.
        # edge cases:
            # neg ints?
            # list is never empt
        
        def binary_search(left, right):

            if left > right:
                return -1

            mdpt = (right + left) // 2

            if target > nums[mdpt]:
                return binary_search(mdpt + 1, right)
            elif target < nums[mdpt]:
                return binary_search(left, mdpt - 1)
            else:
                return mdpt



        return binary_search(0, len(nums) - 1)