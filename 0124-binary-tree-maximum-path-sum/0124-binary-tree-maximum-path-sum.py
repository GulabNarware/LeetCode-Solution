# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        
        sm=float('-inf')

        def cal(node):
            nonlocal sm

            if not node:
                return 0

            left=cal(node.left)
            if left<0:
                left=0


            right= cal(node.right)
            if right<0:
                right=0

            sm=max(sm,left+node.val+right)

            return node.val+max(left,right)

        cal(root)
        return sm
