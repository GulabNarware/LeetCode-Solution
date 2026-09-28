class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        

        l=[]

        for i in range(1,int(n//2)+1):
            if n%i==0:
                l.append(i)

        l.append(n)

        return -1 if len(l)<k else l[k-1] 


        