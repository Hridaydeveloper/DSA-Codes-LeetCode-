class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for p in range(len(nums) - 3):
            if p > 0 and nums[p] == nums[p - 1]:
                continue
            for k in range(p + 1, len(nums) - 2):
                if k > p + 1 and nums[k] == nums[k - 1]:
                    continue
                i = k + 1
                j = len(nums) - 1

                while i < j:
                    total = nums[p] + nums[k] + nums[i] + nums[j]

                    if total == target:
                        res.append([nums[p], nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1

                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1

                    elif total < target:
                        i += 1
                    else:
                        j -= 1

        return res

