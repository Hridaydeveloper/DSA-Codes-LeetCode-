# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.stack = []

        def postorder(root):
            if root is None:
                return
            
            postorder(root.left) #Left subtree
            postorder(root.right) #Right subtree

            self.stack.append(root.val) #Stores root or node value

        postorder(root)
        return self.stack
        
