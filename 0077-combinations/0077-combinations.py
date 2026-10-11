class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        #2^n complexity:-

        # a =[i for i in range(1,n+1)]

        # result=[]

        # def sq(indx,count):

        #     if len(count)==k:
        #         result.append(count.copy())
        #         return 

        #     if len(count)>k:
        #         return 
        #     if indx>=len(a):
        #         return

        #     count.append(a[indx])

        #     sq(indx+1,count)
        #     count.pop()

        #     sq(indx+1,count)

        # sq(0,[])
        # return result
#--------------------------------------------------------------

        #O(n*k)
        result=[]

        def backtrack(start,count):
            if len(count)==k:
                result.append(count.copy())
                return 

            for num in range(start,n+1):
                count.append(num)
                backtrack(num+1,count)
                count.pop()

        backtrack(1,[])

        return result

            



