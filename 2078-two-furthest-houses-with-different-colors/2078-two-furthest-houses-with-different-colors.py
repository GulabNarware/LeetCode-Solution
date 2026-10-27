class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        left=0
        right=1

        mx=float('-inf')

        while left<=right and left <len(colors) and right <len(colors):

            if colors[left] != colors[right]:

                mx=max(abs(left-right),mx)
                
                right +=1

            
            elif colors[left]==colors[right]:
            
                right+=1

            if right==len(colors):
                left+=1
                right=left+1
            


        return mx
        