class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        list_ele=[i for i in range(1,10)]

        result=[]

        def backtrack(ind,total,subset):

            if total ==n and len(subset)==k:
                result.append(subset.copy())

                return 

            if total>n or len(subset)>k:
                return 

            if ind>=len(list_ele):
                return 


            subset.append(list_ele[ind])
            sum_ele=total+list_ele[ind]

            backtrack(ind+1,sum_ele,subset)

            subset.pop()

            backtrack(ind+1,total,subset)

        backtrack(0,0,[])
        return result


        