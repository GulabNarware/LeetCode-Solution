class Solution:
    def primePalindrome(self, n: int) -> int:
        import math
        # if n==1:
        #     return 2

        # for i in range(n,(10**8)+1):
        #     is_prime=True

        #     for j in range(2,int(i**0.5)+1):
        #         if i%j==0:
        #             is_prime=False

        #             break
        #     if is_prime:
        #         if str(i)==str(i)[::-1]:
        #             return i

        def prime(no):
            is_prime=True
            for i in range(2,int(no**0.5)+1):
                if no%i==0:
                    is_prime=False

                    break

            return is_prime

        def primepalindrome(no):
            no=11 if n==1 else n
            while True:
                if ((no > 1000 and no < 10000) or
                    (no > 100000 and no < 1000000) or
                    (no > 10000000 and no < 100000000)):

                    no=pow(10,math.ceil(math.log10(no)))
                    continue

                if prime(no) and str(no)==str(no)[::-1]:
                    return no
                no+=1

        if n==1:
            return 2
        return primepalindrome(n)
