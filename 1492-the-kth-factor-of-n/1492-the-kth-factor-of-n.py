class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
    # O(n) space or O(n) time complexity

        # l=[]

        # for i in range(1,int(n//2)+1):
        #     if n%i==0:
        #         l.append(i)

        # l.append(n)

        # return -1 if len(l)<k else l[k-1] 

#-------------------------------------------------
        fac=[]
        
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                fac.append(i)

                if i!= n//i:
                    fac.append(n//i)
        fac.sort()

        return -1 if len(fac)<k else fac[k-1]