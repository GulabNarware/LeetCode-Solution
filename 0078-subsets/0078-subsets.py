class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result=[]

        subset=[]

        def sebseq(indx,subset):

            if indx >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[indx])
            sebseq(indx+1,subset)
            subset.pop()

            sebseq(indx+1,subset)

        sebseq(0,subset)

        return result

























        