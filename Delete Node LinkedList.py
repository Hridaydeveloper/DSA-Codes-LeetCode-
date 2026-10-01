class List:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

#Create the Linked List
head = List(1)
head.next = List(2)
head.next.next = List(3)
head.next.next.next = List(4)

n = 4
curr = head
count = 1
if n == 1:
  head = curr.next
else:
  while curr:
    if count + 1 == n:
      curr.next = curr.next.next
      break
    curr = curr.next
    count += 1
  
# Print the List
curr = head
while curr:
  print(curr.val, end = " --> ")
  curr = curr.next
print(None)
