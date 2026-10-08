class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        
        dist=set()

        dist.add(self.cal(p1,p2))
        dist.add(self.cal(p1,p3))
        dist.add(self.cal(p1,p4))
        dist.add(self.cal(p2,p3))
        dist.add(self.cal(p2,p4))
        dist.add(self.cal(p3,p4))
        return 0 not in dist and len(dist)==2

    
    def cal(self,a,b):
        return (a[0]-b[0])**2+(a[1]-b[1])**2

