# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_value=float('-inf')

        def max_path(node):
            nonlocal max_value

            if not node:
                return 0

            lf=max_path(node.left)
            if lf<0:
                lf=0

            rt=max_path(node.right)


            if rt<0:
                rt=0

            max_value=max(max_value,lf+node.val+rt)

            return node.val + max(lf,rt)

        max_path(root)

        return max_value