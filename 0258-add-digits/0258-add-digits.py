class Solution:
    def addDigits(self, num: int) -> int:
        if num<=9:
            return num

        while num>9:

            n=num%10
            num//=10
            num+=n

        return num