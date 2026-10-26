# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        if head is None or head.next is None:
            return head

        length = 0
        curr = head
        end_node = None

        while curr:
            end_node = curr
            length += 1
            curr = curr.next

        k = k % length

        if k == 0:
            return head
        
        end_node.next = head

        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        head = curr.next
        curr.next = None

        return head


        
