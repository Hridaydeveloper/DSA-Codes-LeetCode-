"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.stack = []

        def postorder(node):
            if node is None:
                return 

            if node.children:
                for child in node.children:
                    postorder(child)



            self.stack.append(node.val)


        postorder(root)

        return self.stack
        
