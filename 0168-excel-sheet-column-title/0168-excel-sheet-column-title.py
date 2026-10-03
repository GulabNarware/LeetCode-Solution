class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        def convert(n):
            res=""
            

            while n>0:
                n=n-1
                
                
                rem=n%26
                n//=26

                ans=chr(65 +rem)
                res=ans+res

            return res

        return convert(columnNumber)
            