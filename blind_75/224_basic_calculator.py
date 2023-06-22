class Solution:
    def calculate(self, s: str) -> int:
        # input: string representing valid math expression
        # output: result of expression
        # constraints:
            # 1 <= s.length <= 3 * 10^5
            # s consists of digits, '+', '-', '(', ')', and ' '.
            # s represents a valid expression.
            # '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
            # '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
            # There will be no two consecutive operators in the input.
            # Every number and running calculation will fit in a signed 32-bit integer.
        # edge cases:
            # white spaces
            # parentheses -> implies order of operations
            # always a valid expression
        
        s = s.replace(" ", "")

        total = 0
        sign = 1
        stack = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                total += sign * num

            elif s[i] == "(":
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
                i += 1
            elif s[i] == ")":
                total = stack.pop() * total + stack.pop()
                i += 1
            elif s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "-":
                sign = -1
                i += 1
            else:
                i += 1

        return total