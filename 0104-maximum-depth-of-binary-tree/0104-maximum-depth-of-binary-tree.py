# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        mx=0
        if not root:
            return 0
        def depth(node,count):
            nonlocal mx
            if not node:
                return 0
            if count>mx:
                mx=count

            if node.val is None:
                return 0


            depth(node.left,count+1)
            depth(node.right,count+1)

        depth(root,0)
        return mx+1




        