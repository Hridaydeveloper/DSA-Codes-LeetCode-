# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = None 
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        count = 1
        curr = prev

        if n == 1:
            prev = prev.next
        else:
            while curr:
                if count + 1 == n:
                    curr.next = curr.next.next
                    break
                curr = curr.next
                count += 1

        curr = prev
        res = None

        while curr:
            next_node = curr.next
            curr.next = res
            res = curr
            curr = next_node
            
        return res


# Or, 

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        #Find the length
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if length == n:
            return head.next

        #Find the nth node before the target
        curr = head
        for i in range(length - n - 1):
            curr = curr.next

        #Remove the node
        curr.next = curr.next.next

        return head

# Or, 
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        for i in range(n):
            curr = curr.next

        if curr is None:
            return head.next

        j = curr
        i = head

        while j != None and j.next != None:
            j = j.next
            i = i.next

        i.next = i.next.next

        return head


            
