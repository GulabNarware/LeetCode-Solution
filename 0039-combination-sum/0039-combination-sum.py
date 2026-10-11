class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result=[]

        count=[]

        def sq(indx,total,count):
            if indx>=len(candidates):
                return 

            if total==target:
                result.append(count.copy())
                return 

            if total>target:
                return 
            total+=candidates[indx]
            count.append(candidates[indx])
            sq(indx,total,count)

            a=count.pop()
            total-=a

            sq(indx+1,total,count)

        sq(0,0,count)
        return result

            