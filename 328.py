# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:

        if head is None:
            return None

        res = ListNode(0)
        curr = res

        current = head
        while current:
            curr.next = ListNode(current.val)
            curr = curr.next

            if current.next:
                current = current.next.next
            else:
                break

        current = head.next
        
        while current:
            curr.next = ListNode(current.val)
            curr = curr.next

            if current.next:
                current = current.next.next
            else:
                break

        return res.next
