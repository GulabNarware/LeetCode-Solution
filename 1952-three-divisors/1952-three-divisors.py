class Solution:
    def isThree(self, n: int) -> bool:
        num=int(n**0.5)
        if num*num!=n:
            return False
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
        

        