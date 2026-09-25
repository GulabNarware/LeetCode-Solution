class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        pw=0
        num=0

        while n>0 and num<=n:

            if 2**pw==n:
                return True

            pw+=1

            num=2**pw

        return False