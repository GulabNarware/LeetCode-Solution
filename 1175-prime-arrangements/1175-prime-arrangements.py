class Solution:
    import math
    def numPrimeArrangements(self, n: int) -> int:
        
        

        count_prime=0
        count_Non_prime=1

        for i in range(2,n+1):
            is_prime=True

            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    count_Non_prime+=1
                    is_prime=False
                    break

            if is_prime:
                count_prime+=1
        result=math.factorial(count_prime) * math.factorial(count_Non_prime)
        return result% (10**9 + 7)
        