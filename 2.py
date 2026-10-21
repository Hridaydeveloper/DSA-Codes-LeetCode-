# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None and l2 is None:
            return None

        #Get the nodes val of l1 in array
        curr = l1
        num1 = []
        while curr:
            num1.append(str(curr.val))
            curr = curr.next

        #Get the nodes val of l2 in array
        curr = l2
        num2 = []
        while curr:
            num2.append(str(curr.val))
            curr = curr.next

        #Add the integer numbers of l1 and l2
        n1 = int("".join(num1[::-1]))
        n2 = int("".join(num2[::-1]))

        result = n1 + n2

        head = None

        for digit in str(result):
            node = ListNode(int(digit))
            node.next = head
            head = node

        return head
        
        
        
