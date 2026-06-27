class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]

        # def solve(ind,total,res):

        #     if ind>=len(candidates):
        #         if total==target:
                    
        #             result.append(res.copy())
        #         return 
        #     if total>target:
        #         return 
        #     if total==target:
               

        #         result.append(res.copy())

        #         return 
        #     #pick
        #     res.append(candidates[ind])
        #     sum_ele=total+candidates[ind]
        #     solve(ind+1,sum_ele,res)

        #     #not pick
        #     res.pop()
            
        #     #remove duplicate 
        #     while ind+1<len(candidates) and candidates[ind]==candidates[ind+1]:
        #         ind+=1
        #         continue
        #     solve(ind+1,total,res)

        # solve(0,0,[])
        # return result


        #second method 

        def backtrack(ind,total,subset):

            if total==0:
                result.append(subset.copy())

            if total<0:
                return 
            if ind>=len(candidates):
                return

            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue

                subset.append(candidates[i])
                sum_ele=total-candidates[i]
                backtrack(i+1,sum_ele,subset)
                subset.pop()

        backtrack(0,target,[])

        return result


            
        