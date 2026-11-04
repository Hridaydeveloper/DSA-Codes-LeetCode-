class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        i = len(temperatures) - 1
        answer = [0]*len(temperatures)

        while i >= 0:
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if len(stack) == 0:
                day = 0
            else:
                day = stack[-1] - i

            stack.append(i)
            answer[i] = day

            i -= 1

        return answer
