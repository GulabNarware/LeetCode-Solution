class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        h={}

        for i in deck:
            h[i]=h.get(i,0)+1

        #using Euclidean Algorithm

        values=list(h.values())

        gcd=values[0]

        for c in values[1:]:

            while c!=0:
                gcd,c=c,gcd%c

        return gcd >=2
