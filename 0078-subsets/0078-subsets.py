class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        res=[]

        

        def fun(indx,subset):

            if indx>=len(nums):

                res.append(subset.copy())
                return

            subset.append(nums[indx])

            fun(indx+1,subset)

            subset.pop()

            fun(indx+1,subset)


        fun(0,[])
        return res

        