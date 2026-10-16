# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx=0
        def dm(node):
            nonlocal mx

            if node is None:
                return 0


            left=dm(node.left)
            right=dm(node.right)

            if left+right>mx:
                mx=left+right

            return 1+max(left,right)
        dm(root)
        return mx
