class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result=[]

        count=[]

        def sq(indx,count):
            if indx>=len(candidates):
                return 

            if sum(count)==target:
                result.append(count.copy())
                return 

            if sum(count)>target:
                return 
            count.append(candidates[indx])
            sq(indx,count)

            count.pop()

            sq(indx+1,count)

        sq(0,count)
        return result

            