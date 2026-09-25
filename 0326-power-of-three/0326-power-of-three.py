class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        pw=0
        num=0

        while n>0 and num<=n:

            if 3**pw==n:
                return True

            pw+=1
            num=3**pw

        return False