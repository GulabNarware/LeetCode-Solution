class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq={}
        
        for i in range(1,n+1):
            sum_no=0
            f=i
            while f>0:
                digit=f%10

                sum_no+=digit

                f=f//10

            freq[sum_no]=freq.get(sum_no,[])+[i]
        
        larger=float('-inf')
        for x in freq:
            if len(freq[x])>larger:
                larger=len(freq[x])
        count=0
        for x in freq:
            if len(freq[x])==larger:
                count+=1
                
        return count

        



