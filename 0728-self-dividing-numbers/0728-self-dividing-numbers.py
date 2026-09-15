class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]

        for i in range(left,right+1):
            
            is_div=True
            j=i
            while j>0:
                digit=j%10
                 
                if digit==0 or i%digit!=0:
                    is_div=False
                    break

                j=j//10
            if is_div:
                l.append(i)

        return l
            

                
