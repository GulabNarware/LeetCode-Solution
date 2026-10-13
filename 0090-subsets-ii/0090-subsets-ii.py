class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result=[]
        nums.sort()
        def backtrack(indx,count):
            if indx>=len(nums):
                
                result.append(count.copy())

                return 

            count.append(nums[indx])
            backtrack(indx+1,count)
            count.pop()
            indx+=1
            while indx<len(nums) and indx!=0 and nums[indx]==nums[indx-1] :
                indx+=1

            backtrack(indx,count)

        backtrack(0,[])

        return result


            