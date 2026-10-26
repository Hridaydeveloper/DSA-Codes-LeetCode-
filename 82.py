# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        hashmap = {}
        res = ListNode(0)
        current = res
        curr = head

        while curr:
            if curr.val not in hashmap:
                hashmap[curr.val] = 1
            else:
                hashmap[curr.val] += 1

            curr = curr.next

        curr = head
        while curr:
            if hashmap[curr.val] == 1:
                current.next = curr
                current = current.next

            curr = curr.next

        current.next = None

        return res.next

                

