# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        self.check=True
        mn=float('-inf')
        mx=float('inf')
        def helper(node,mn,mx):

            if not node:
                return 
            if not mn<node.val<mx:
                self.check=False
                return          

            helper(node.left,mn,node.val)

            helper(node.right,node.val,mx)

        helper(root,mn,mx)
        return self.check


