# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def sr(node):
            if not node:
                return node
            if node.val==val:
            
                return node
            if val > node.val:
                return sr(node.right)

            if val<node.val:
                return sr(node.left)

        return sr(root)
        

            