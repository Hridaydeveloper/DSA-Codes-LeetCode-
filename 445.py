# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        if l1 is None and l2 is None:
            return None
        
        left1 = None
        curr = l1

        while curr:
            next_node = curr.next
            curr.next = left1
            left1 = curr
            curr = next_node

        left2 = None
        curr = l2

        while curr:
            next_node = curr.next
            curr.next = left2
            left2 = curr
            curr = next_node

        carry = 0

        head = ListNode(0)
        curr = head

        while left1 or left2 or carry:
            if left1:
                n1 = left1.val
            else:
                n1 = 0

            if left2:
                n2 = left2.val
            else:
                n2 = 0


            ans = n1 + n2 + carry

            digit = ans % 10
            carry = ans // 10

            curr.next = ListNode(digit)
            curr = curr.next

            if left1:
                left1 = left1.next

            if left2:
                left2 = left2.next

        prev = None
        current = head.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

        
