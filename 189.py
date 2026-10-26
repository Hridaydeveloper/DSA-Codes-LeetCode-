class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        k = k % len(nums)
        i = len(nums) - k

        while i < len(nums):
            res.append(nums[i])
            nums.pop(i)

        nums[:] = res + nums
        
