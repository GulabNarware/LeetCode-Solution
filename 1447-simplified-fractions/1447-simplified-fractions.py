class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        s=set()
        l=[]

        for i in range(2,n+1):

            for j in range(1,n):

                if j%i!=0 and j/i not in s and i>j:
                    a=j/i

                    s.add(a)

                    l.append(f"{j}/{i}")

        return l

