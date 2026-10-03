class Solution:
    def integerBreak(self, n: int) -> int:
        # count=0
        # sum_ele=0

        if n==2:
            return 1
        if n==3:
            return 2

#-----------------------------------------

        # for i in range(n):
        #     sum_ele+=3
        #     if sum_ele<n:
        #         count+=1

        #     else:
        #         break
#----------------------------------------------------
        threes=n//3
        rem=n%3

        if rem==1:
            threes-=1
            return (3**threes)*4
        elif rem==2:
            return (3**threes)*rem
        else:
            return 3**threes

        
