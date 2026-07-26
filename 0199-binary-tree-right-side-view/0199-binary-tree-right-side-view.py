# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        queue=deque()
        result=[]
        queue.append(root)
        while queue:
            level=len(queue)
            
            for i in range(level):
                ele=queue.popleft()
               
                if i==level-1:
                    result.append(ele.val)

                if ele.left:
                    queue.append(ele.left)

                if ele.right:
                    queue.append(ele.right)

        return result



                


            

            



            
        