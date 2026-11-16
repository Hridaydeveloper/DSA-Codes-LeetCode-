# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k <= 1:
            return head
        
        curr = head
        length = 0  # Fix 1: Start at 0 instead of 1
        while curr:
            length += 1
            curr = curr.next

        n = length // k
        
        curr = head             # Fix 2: Initialize curr = head OUTSIDE the loop
        prev_group_tail = None  # Fix 3: Track the tail of the previous reversed group
        new_head = None         # Fix 4: Save the head of the very first reversed group

        for i in range(n):
            group_head = curr
            prev = None
            count = 0
            
            while curr and k > count:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                count += 1
                
            group_head.next = curr

            # Fix 5: Connect the previous group's tail to this group's new head (prev)
            if i == 0:
                new_head = prev
            else:
                prev_group_tail.next = prev
                
            prev_group_tail = group_head

        return new_head
