class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        a =[i for i in range(1,n+1)]

        result=[]

        def sq(indx,count):

            if len(count)==k:
                result.append(count.copy())
                return 

            if len(count)>k:
                return 
            if indx>=len(a):
                return

            count.append(a[indx])

            sq(indx+1,count)
            count.pop()

            sq(indx+1,count)

        sq(0,[])
        return result

