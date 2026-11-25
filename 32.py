class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return 0
        else:
            longest = 0
            stack = [-1]

            for i in range(len(s)):
                ch = s[i]

                if ch == '(':
                    stack.append(i)
                    
                else:
                    stack.pop()

                    if len(stack) == 0:
                        stack.append(i)
                    else:
                        curr_window = i - stack[-1]
                        longest = max(curr_window, longest)

            return longest
