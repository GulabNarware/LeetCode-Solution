class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add=0
        multi=1

        while n>0:
            a=n%10
            add+=a
            multi*=a
            n=n//10

        return multi-add