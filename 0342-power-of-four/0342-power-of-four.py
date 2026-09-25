class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n<=0:
            return False
        num=0
        pw=0
        while num<=n:
            if 4**pw==n:
                return True
            num=4**pw
            pw+=1
            
        return False