from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # input: list of integers representing asteroids in a row
        # output: new list after collisions; collisions happen when positive and negative run into each other; chain collisions happen
        # constraints: 
            # 2 <= asteroids.length <= 104
            # -1000 <= asteroids[i] <= 1000
            # asteroids[i] != 0
        # edge cases:
            # positive and negative numbers having same values
            # all positive or all negative values
            # length of asteroids is always at least 2
        
        stack = []

        i = 0
        while i < len(asteroids):
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] + asteroids[i] < 0:
                    stack.pop()
                elif stack[-1] + asteroids[i] > 0:
                    i += 1
                else: # if they're equal
                    stack.pop()
                    i += 1
            else:
                stack.append(asteroids[i])
                i += 1

        return stack