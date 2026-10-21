class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        # count=0
        # left=0
        # right=0
        # sm=nums[left]

        # while left<=right and left<len(nums) and right<len(nums):

        #     if goal==sm:
        #         count+=1

        #         if right+1 <= len(nums)-1:
        #             sm+=nums[right]

        #             right+=1

        #         else:
        #             left+=1
        #             left=right
        #             sm=nums[left]

        #     elif right==len(nums)-1 and left+1<len(nums):
        #         left+=1
        #         right=left
        #         sm=nums[left]
        #     elif sm<goal:
        #         sm+=nums[right]
        #         right+=1

        #     else:
        #         sm-=nums[left]
        #         left+=1


        # return count


        h={}

        h[0]=1

        result=0
        sm=0

        for r in nums:
            sm+=r

            if sm-goal in h:
                result+=h[sm-goal]

            h[sm]=h.get(sm,0)+1

        return result

            

            
