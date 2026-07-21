# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []


        result=[]
        queue=deque([])
        queue.append(root)

        while len(queue)!=0:
            level=[]

            for _ in range(len(queue)):
                ele=queue.popleft()
                level.append(ele.val)

                if ele.left is not None :
                    queue.append(ele.left)

                if ele.right is not None :

                    queue.append(ele.right)

            result.append(level)

        return result


        