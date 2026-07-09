class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()

        s.sort()
        right=0
        left=0
        n=len(g)
        m=len(s)
        total=0
        while left<m and right<n:

            if g[right]<=s[left]:
                right+=1
                total+=1

            left+=1

        return total



