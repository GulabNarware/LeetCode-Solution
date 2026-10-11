class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        a=[i for i in range(1,10)]

        result=[]

        def sq(indx,total,sub):
            if indx>=len(a) :
                if k==len(sub) and total==n:
                    result.append(sub.copy())
                return 

            if n==total and k==len(sub):
                result.append(sub.copy())
                return 

            if total> n or len(sub)>k:
                return 

            sub.append(a[indx])

            ele=total+a[indx]

            sq(indx+1,ele,sub)

            sub.pop()

            sq(indx+1,total,sub)

        sq(0,0,[])

        return result

            
