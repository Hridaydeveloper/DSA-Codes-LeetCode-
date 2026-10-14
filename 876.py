# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
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
        if k == 1:
            return head
        else:
            count = 1
            curr = head
            while curr:
                if count == k:
                    return curr
                curr = curr.next
                count += 1


#Or,

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        #Find the length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        #Find the middle element
        curr = head
        for i in range(length//2):
            curr = curr.next

        return curr


#Or,

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow
                
