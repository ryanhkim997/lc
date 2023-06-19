import operator
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # input: array of strings (tokens) where each string is an RPN arithmetic expression
        # output: int that represents the calculated value of the expression
        # constraints:
        # edge cases:
            # always valid arithmetic expression
            # length of tokens is always at least one; tokens being of length 1 is an edge case here
            # no division by zero
            # division always truncated (floored result)
            # division implies that order of numbers in operation matters
        
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "/": operator.truediv,
            "*": operator.mul
        }

        for i in tokens:
            # if we have an operator:
            if i in operators:
                # pop off stack twice and store those, and make sure that second pop is the first integer in operation
                second = stack.pop()
                first = stack.pop()
                # perform operation
                stack.append(int(operators[i](first, second)))
                # append the result of the operation to stack
            # else
            else:
                stack.append(int(i))
                # append i

        return stack[-1]

# Notes:
    # notice int call on line 31. this floors the operation and truncates it towards zero if the value is fractional.