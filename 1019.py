# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:

        if head is None:
            return None

        result = []

        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next

        ans = [0]*len(result)
        stack = []
        i = len(result) - 1

        while i >= 0:
            while stack and result[i] >= result[stack[-1]]:
                stack.pop()

            if len(stack) == 0:
                greater = 0
            else:
                greater = result[stack[-1]]

            stack.append(i)
            ans[i] = greater

            i -= 1

        return ans

        
