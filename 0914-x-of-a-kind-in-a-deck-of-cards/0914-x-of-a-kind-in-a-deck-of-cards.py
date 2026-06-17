class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        
        # d={}

        # for i in deck:
        #     d[i]=d.get(i,0)+1

        # m=min(d.values())
        # if m>1:
        #     for j in range(2,m+1):
        #         for count in d.values():
        #             if count%j!=0:
        #                 break

        #         else:
        #             return True
        # else:
        #     return False


   

        d = {}

        for i in deck:
            d[i] = d.get(i, 0) + 1

        m = min(d.values())

        if m > 1:
            for j in range(2, m + 1):

                for count in d.values():
                    if count % j != 0:
                        break

                else:
                    return True

        return False
