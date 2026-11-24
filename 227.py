class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(float(stack.pop()) / num))

                op = ch
                num = 0

        return sum(stack)
