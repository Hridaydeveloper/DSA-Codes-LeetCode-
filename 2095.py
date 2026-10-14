# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        #Find the length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        #Find the middle element
        k = 0
        if length % 2 == 0:
            k = (length // 2) + 1
        else:
            k = (length // 2) + 1
        #Return the node value
        curr = head
        if k == 1:
            return None
        else:
            count = 1
            curr = head
            while curr:
                if count + 1 == k:
                    curr.next = curr.next.next
                curr = curr.next
                count += 1
        return head
        
