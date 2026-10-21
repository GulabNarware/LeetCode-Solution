class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        count=0
        left=0
        right=0
        sm=0
        zeros=0

        while right <len(nums):

            sm+=nums[right]

            while left< right and (nums[left]==0 or sm>goal):
                if nums[left]==0:
                    zeros+=1     
                else:
                    zeros=0
                sm-=nums[left]
                left+=1

            if sm==goal:
                count+=1+zeros
            right+=1

        return count


#prefix and hashmap:-

        # h={}

        # h[0]=1

        # result=0
        # sm=0

        # for r in nums:
        #     sm+=r

        #     if sm-goal in h:
        #         result+=h[sm-goal]

        #     h[sm]=h.get(sm,0)+1

        # return result

            

            
