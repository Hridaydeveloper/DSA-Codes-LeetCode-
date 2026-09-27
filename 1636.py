class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        sorted_keys = sorted(hashmap, key=lambda x: (hashmap[x], -x))

        res = []
        i = 0
        while i < len(sorted_keys):
            if sorted_keys[i] in hashmap:
                if hashmap[sorted_keys[i]] != 0:
                    res.append(sorted_keys[i])
                    hashmap[sorted_keys[i]] -= 1
                elif hashmap[sorted_keys[i]] == 0:
                    i += 1
                else:
                    continue
        return res
