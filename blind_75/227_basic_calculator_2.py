# potentially n^2 time.. could be a little better and simplified
class Solution:
    def calculate(self, s: str) -> int:

        def eval_expression():
            second_val = values.pop()
            first_val = values.pop()
            operator = operators.pop()

            if operator == "+":
                values.append(first_val + second_val)
            elif operator == "-":
                values.append(first_val - second_val)
            elif operator == "*":
                values.append(first_val * second_val)
            elif operator == "/":
                values.append(int(first_val / second_val))

        def precedence(operator):
            if operator in "*/":
                return 0
            else:
                return 1

        s = s.replace(" ", "")

        values = []
        operators = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                values.append(num)
            elif s[i] in "+-*/":
                while (operators and precedence(operators[-1]) <= precedence(s[i])):
                    eval_expression()
                operators.append(s[i])
                i += 1
            else:
                i += 1
            
        while operators:
            eval_expression()
    
        return values[-1]


# better time performance, worse space

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = "+"

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-/*" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    stack[-1] = int(stack[-1] / num)
                num = 0
                sign = s[i]
            
        return sum(stack)