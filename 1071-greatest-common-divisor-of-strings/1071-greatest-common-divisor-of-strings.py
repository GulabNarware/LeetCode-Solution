class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1+str2 != str2+str1:
            return ""


        ln1=len(str1)
        ln2=len(str2)

        def gcd(a,b):

            while b!=0:
                a,b=b,a%b

            return a

        a=gcd(ln1,ln2)

        return str1[:a]