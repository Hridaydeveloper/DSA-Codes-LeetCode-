# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):

        if head is None or head.next is None:
            return head

        # Pass 1: values < x
        res = ListNode(0)
        current = res

        curr = head
        while curr:
            if curr.val < x:
                current.next = ListNode(curr.val)
                current = current.next

            curr = curr.next

        #  Pass 2: values >= x
        curr = head
        while curr:
            if curr.val >= x:
                current.next = ListNode(curr.val)
                current = current.next
            curr = curr.next

        return res.next

# Or, 

class Solution(object):
    def partition(self, head, x):
      
        if head is None or head.next is None:
            return head
        
        head1 = ListNode(0)
        left = head1

        head2 = ListNode(0)
        right = head2

        curr = head
        while curr:
            next_node = curr.next
            if curr.val < x:
                left.next = curr
                left = left.next

            else:
                right.next = curr
                right = right.next

            curr = curr.next

        right.next = None
        left.next = head2.next

        return head1.next

