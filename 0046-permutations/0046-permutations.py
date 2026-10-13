class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=[]

        ln=len(nums)


        def backtrack(indx,count):
            if indx>=ln:
                result.append(count.copy()) 
                return

            for i in range(indx,len(count)):

                #choice

                count[i],count[indx]=count[indx],count[i]

                #exploire

                backtrack(indx+1,count)

                #backtrack

                count[i],count[indx]=count[indx],count[i]

        backtrack(0,nums)
        return result


