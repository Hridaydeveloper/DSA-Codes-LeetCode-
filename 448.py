class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1

        ans = []
        n = 1
        for i in range(len(nums)):
            if n not in hashmap:
                ans.append(n)
            n += 1

        return ans
