class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]

        def solve(ind,total,res):

            if ind>=len(candidates):
                if total==target:
                    
                    result.append(res.copy())
                return 
            if total>target:
                return 
            if total==target:
               

                result.append(res.copy())

                return 

            res.append(candidates[ind])

            sum_ele=total+candidates[ind]

            solve(ind+1,sum_ele,res)

            res.pop()
            
           

            while ind+1<len(candidates) and candidates[ind]==candidates[ind+1]:
                ind+=1
                continue




            solve(ind+1,total,res)

        solve(0,0,[])
        return result



            
        