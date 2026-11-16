class Node:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 2
prev = None
curr = head

length = 2
while length > 0: 
  for _ in range(k):
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
  length -= 1

curr = prev
while curr:
  print(curr.val, end = " -> ")
  curr = curr.next

print(next_node.next.val)
