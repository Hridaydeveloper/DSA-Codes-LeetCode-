class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [0]*len(nums)
        i = len(nums) -1
        while i >= 0:
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if len(stack) == 0:
                greater = -1
            else:
                greater = stack[-1]

            stack.append(nums[i])
            ans[i] = greater

            i -= 1

        i = len(nums) -1
        while i >= 0:
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if len(stack) == 0:
                greater = -1
            else:
                greater = stack[-1]

            stack.append(nums[i])
            ans[i] = greater

            i -= 1

        return ans
        
