class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        # s=set()
        # l=[]

        # for i in range(2,n+1):

        #     for j in range(1,i):

        #         if j%i!=0 and j/i not in s and i>j:
        #             a=j/i

        #             s.add(a)

        #             l.append(f"{j}/{i}")

        # return l

        #gcd version

        def gcd(a,b):
            while a>0 and b>0:
                if a>b:
                    a=a%b
                else:
                    b=b%a

            return a if a>0 else b

        l=[]
        for denomitor in range(2,n+1):

            for numerator in range(1,denomitor):

                if gcd(denomitor,numerator)==1:
                    l.append(f'{numerator}/{denomitor}')

        return l
