class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        hashmap = {}
        i = len(nums2) - 1

        while i >= 0:
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if not stack:
                greater = -1
            else:
                greater = stack[-1]

            stack.append(nums2[i])
            hashmap[nums2[i]] = greater

            i -= 1

        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                nums1[i] = hashmap[nums1[i]]

        return nums1
            
