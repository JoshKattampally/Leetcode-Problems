# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        in_order = []
        stack, p = [], root
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                in_order.append(p.val)
                p = p.right
        return in_order
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        