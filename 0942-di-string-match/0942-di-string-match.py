class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        I=0
        D=None
        ans=[]
        i=0
        while i< len(s):
            if s[i]=="I":
                ans.append(I)
                I+=1
                i+=1

            else:
                if D is None:
                    D=len(s)

                    ans.append(D)

                else:
                    D-=1
                    ans.append(D)

                i+=1

        if s[i-1]=="I":
            
            ans.append(I)

        else:
            
            ans.append(D-1)


        return ans

        