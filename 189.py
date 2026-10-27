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

Or, 

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        k = k % len(nums) 

        #Reverse the entire array
        nums.reverse()
        
        #Reverse the first kth elements
        nums[:k] = reversed(nums[:k])

        #Reverse the last elements after kth
        nums[k:] = reversed(nums[k:])

        
