# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.result=[]

        def inord(node):
            if not node:
                return
            inord(node.left)
            self.result.append(node.val)
            inord(node.right)
        
        inord(root)
        return self.result
    