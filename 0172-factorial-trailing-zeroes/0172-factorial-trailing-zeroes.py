class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        # total_zero=0
        # fact=1

        # for i in range(n,0,-1):
        #     fact*=i
        # its_true=True
        # while fact>0:
        #     a=fact%10
        #     if a==0 and its_true:
        #         total_zero+=1
        #     else:
        #         its_true=False

        #     fact=fact//10

        # return total_zero

        sum_zero=0

        while (n//5)>0:
            sum_zero+=n//5

            n=n//5

        return sum_zero

