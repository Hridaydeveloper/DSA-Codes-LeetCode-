class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Handle base case
        if head and head.next is None:
            return None

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            #Check cycle exist
            if fast == slow:
                #If cycle exist move the slow to head 
                slow = head
                break
        else:
            return None
        #Now move the both slow and fast one step until both stops at a node
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return fast
