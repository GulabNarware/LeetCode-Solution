class Solution:
    def reverseWords(self, s: str) -> str:

        ans=""
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and i+1<len(s)-1 and s[i+1]==" ":
                continue
            
            elif s[i]==" " and (i==len(s)-1 or i==0):
                continue

            else:
                if s[i]==" ":
                    ans=" "+ans

                else:
                    ans=s[i]+ans
        
        result=""
        c=len(ans)-1

        for i in range(len(ans)-1,-1,-1):

            if ans[i]==" ":
                result=result+" "+ans[i+1:c+1]
                c=i-1
        result=result+" "+ans[0:c+1]
        return result.strip()
