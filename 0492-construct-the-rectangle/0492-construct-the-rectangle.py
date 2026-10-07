class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        fac=[area,1]
        min_Deff=area-1

        for i in range(1,int(area**0.5)+1):
            if area%i==0:
                a=area//i
                if (a-i)<=min_Deff:

                    fac[0]=a
                    fac[1]=i


        return  fac

        
