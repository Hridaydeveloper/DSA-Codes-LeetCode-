class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = Node(0)
a = Node(1)
b = Node(2)

root.left = a
root.right = b

print(root.data)
print(root.left.data)
print(root.right.data)
