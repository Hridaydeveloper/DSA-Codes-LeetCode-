# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        
        #Treverse the Linked List
        res = []
        curr = head

        while curr:
            res.append(curr.val)
            curr = curr.next

        #Reverse the Linked List
        prev = None 
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        i = 0
        curr = prev

        while curr:
            if curr.val != res[i]:
                return False
            
            curr = curr.next
            i += 1

        return True
