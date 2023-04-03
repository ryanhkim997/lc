from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # output: list of all letter combinations the number can represent
            # 2 -> abc
        # input:
            # string representing number from 2-9
        # constraints:
            # 0 <= digits.length <= 4
            # digits[i] is a digit in the range ['2', '9'].
        # edge cases:
            # empty string
            # order does matter in this case; permutations and not combinations
        letter_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        output = []

        if not len(digits):
            return output

        def backtrack(perm, next_digits):
            if not next_digits:
                output.append(perm)
                return

            for letter in letter_mapping[next_digits[0]]:
                backtrack(perm + letter, next_digits[1:])


        backtrack("", digits)
        return output