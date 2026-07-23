# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0

        def height(nodee):
            nonlocal diameter

            if nodee is None:
                return 0

            leftt=height(nodee.left)
            rightt=height(nodee.right)

            diameter=max(diameter,leftt+rightt)

            return 1+max(leftt,rightt)

        height(root)

        return diameter
