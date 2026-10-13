class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        s=set()
        result=[]

        def backtrack(indx,count):

            if indx>=len(count):
                if tuple(count) not in s:
                    result.append(count.copy())
                    s.add(tuple(count))

                return 

            for i in range(indx,len(count)):

                #choice

                count[i],count[indx]=count[indx],count[i]

                #exploiler
                backtrack(indx+1,count)

                #backtrack
                count[i],count[indx]=count[indx],count[i]


        backtrack(0,nums)
        return result