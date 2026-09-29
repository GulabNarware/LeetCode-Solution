class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def base(n,k):
        
            n1=n
            result=0

            while n1>0:
                digit=n1%k

                n1=n1//k

                result+=digit

            return result


        num=base(n,k)


        return num