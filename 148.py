# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:

        if head is None or head.next is None:
            return head

        #Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #Split into two lists
        l1 = head
        l2 = slow.next
        slow.next = None

        l1 = self.sortList(l1)
        l2 = self.sortList(l2)

        i, j = l1, l2
        res = ListNode()
        curr = res

        while i and j:
            if i.val < j.val:
                curr.next = i
                i = i.next
            else:
                curr.next = j
                j = j.next

            curr = curr.next

        if i:
            curr.next = i
        if j:
            curr.next = j

        return res.next

