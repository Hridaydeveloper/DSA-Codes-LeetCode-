class List:
  def __init__(self, val = 0, next = None):
    self.next = next
    self.val = val

#Create the Linked List
head = List(1)
head.next = List(2)
head.next.next = List(3)
head.next.next.next = List(4)

#Insert at the beginning
new = List(0)
new.next = head
head = new

#Insert at the end
new = List(5)
curr = head
while curr.next != None:
  curr = curr.next
curr.next = new

# Print the List
curr = head
while curr:
  print(curr.val, end = " --> ")
  curr = curr.next
print(None)
