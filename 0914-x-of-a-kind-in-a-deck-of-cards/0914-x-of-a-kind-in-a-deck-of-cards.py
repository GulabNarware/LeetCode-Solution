class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        h={}

        for i in deck:
            h[i]=h.get(i,0)+1
        check=min(h.values())

        if check>1:
            for div in range(2,check+1):
                for c in h.values():
                    if c%div!=0:
                        break
                else:
                    return True

        return False