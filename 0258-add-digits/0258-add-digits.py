class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num

        while num>9:
            digit=num%10

            num=num//10

            num+=digit

        return num         

