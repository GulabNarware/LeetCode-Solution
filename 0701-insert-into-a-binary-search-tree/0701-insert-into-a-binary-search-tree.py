# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        self.value=val
        if not root:
            root=TreeNode(self.value)
            return root 

        def BST(r):
            if r.val<self.value:
                if r.right is None:
                    r.right=TreeNode(self.value)
                else:
                    BST(r.right)

            else:
                if r.left is None:
                    r.left=TreeNode(self.value)
                else:
                    
                    BST(r.left)

        BST(root)
        return root
