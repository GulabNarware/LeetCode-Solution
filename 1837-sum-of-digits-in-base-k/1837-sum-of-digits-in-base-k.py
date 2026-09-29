class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def base(n,k):
        
            n1=n
            num=""

            while n1>0:
                digit=n1%k

                n1=n1//k

                num=num+str(digit)

            return int(num[::-1])


        num=base(n,k)

        sum_num=0

        while num>0:
            digit=num%10
            sum_num+=digit
            num=num//10

        return sum_num