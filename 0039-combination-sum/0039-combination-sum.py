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
            e=sol.pop()
            sum_ele=sum_ele-e
            solve(ind+1,sum_ele,sol)
        solve(0,0,[])
        return res



            