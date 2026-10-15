class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        i = list1
        j = list2

        head = ListNode()
        curr = head

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

        return head.next
