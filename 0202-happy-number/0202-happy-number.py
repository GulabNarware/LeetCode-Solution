class Solution:
    def isHappy(self, n: int) -> bool:
        # check=set()
        # def digit(n):
        #     sum_digit=0
        #     while n>0:

        #         digit=n%10
        #         sum_digit+=digit**2
        #         n=n//10

        #     return sum_digit 

        # while n not in check:
        #     check.add(n)
        #     n=digit(n)

            
        #     if n==1:
        #         return True 

        # return False        

        if n==1:
            return True

        def digit(n):
            sum_digit=0

            while n>0:
                d=n%10
                sum_digit+=d**2
                n//=10
            return sum_digit
        hash_map={}

        while n not in hash_map:
            hash_map[n]=1
            n=digit(n)
            if n==1:
                return True


        return False

        


