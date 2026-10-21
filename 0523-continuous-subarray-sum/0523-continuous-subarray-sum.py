class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        if len(nums)==1:return False
        check={}
        check[0]=-1
        sm=0
        for i in range(len(nums)):
            sm+=nums[i]
            n=sm%k
            if n in check :

                if i-check[n]>1:
                    return True
            else:
                check[n]=i
        return False



        