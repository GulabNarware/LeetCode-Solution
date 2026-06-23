class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # for i in range(32):
        #     if n>0 and 2**i==n:
        #         return True

        #     if n<0 and 2**i == (n):
        #         return True

        # else:
        #     return False
        

        if n==0:
            return False
        elif n&(n-1)==0:
            return True

        else:
            return False
