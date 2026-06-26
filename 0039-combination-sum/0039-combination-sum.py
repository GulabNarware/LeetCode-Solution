class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def solve(ind,total,sol):

            if ind>=len(candidates):
                return 
            if target==total:
                res.append(sol.copy())
                return 
            if total>target:
                return 
            sum_ele=total+candidates[ind]
            sol.append(candidates[ind])
            solve(ind,sum_ele,sol)
            sol.pop()
            
            solve(ind+1,total,sol)
        solve(0,0,[])
        return res



            