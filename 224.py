class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        sign = 1  # 1 represents '+', -1 represents '-'
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            elif ch in '+-':
                res += sign * num
                num = 0
                sign = 1 if ch == '+' else -1
            
            elif ch == '(':
                # Save the current result and the sign before '('
                stack.append(res)
                stack.append(sign)
                # Reset for the new sub-expression inside '('
                res = 0
                sign = 1
            
            elif ch == ')':
                # Finish the last number inside ')'
                res += sign * num
                num = 0
                # Apply the sign that was before '(' and add to previous result
                res *= stack.pop()  # sign before '('
                res += stack.pop()  # result before '('

        # Add any leftover number at the end of the string
        return res + (sign * num)
