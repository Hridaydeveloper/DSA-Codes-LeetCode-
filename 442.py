class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        hashmap = {}
        ans = []

        for i in range(len(nums)):
            n = nums[i]
            hashmap[n] = hashmap.get(n, 0) + 1


        for value, freq in hashmap.items():
            if freq >= 2:
                ans.append(value)

        return ans
