class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        if len(nums)==1:return False
        rem_map={}
        rem_map[0]=-1
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            rem=prefix_sum%k
            if rem in rem_map :

                if i-rem_map[rem]>1:
                    return True
            else:
                rem_map[rem]=i
        return False



        
