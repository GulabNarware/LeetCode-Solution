class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """


        if x>=0:
            rev=0
            num=x

            while num>0:
                digit=num%10

                rev=rev*10+digit

                num=num//10
            if rev< -2**31 or rev> 2**31-1:
                return 0
            return rev

        else:
            rev=0
            num=abs(x)

            while num>0:
                digit=num%10

                rev=rev*10+digit

                num=num//10


            if rev< -2**31 or rev> 2**31-1:
                return 0
            return -rev




