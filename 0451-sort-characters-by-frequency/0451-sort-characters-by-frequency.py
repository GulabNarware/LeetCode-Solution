class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1

        sorted_d=dict(sorted(d.items(),key=lambda i:i[1], reverse=True))

        s=""
        for i in sorted_d:
            s=s+sorted_d[i]*i

        return s

            
