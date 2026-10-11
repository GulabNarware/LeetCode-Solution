class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        result=[]
        def sq(indx,total,count):
            if indx>=len(candidates):
                if total==target :
                    result.append(count.copy())
                return 
            if total>target:
                return 
            if total==target:
                result.append(count.copy())

                return 



            count.append(candidates[indx])

            total+=candidates[indx]

            sq(indx+1,total,count)

            a=count.pop()
            total-=a
            while indx+1<len(candidates) and candidates[indx]==candidates[indx+1]:
                indx+=1
                continue

            sq(indx+1,total,count)

        sq(0,0,[])

        return result