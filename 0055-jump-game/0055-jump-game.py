class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_indx=nums[0]

        for i in range(len(nums)):
            if i> max_indx:
                return False

            max_indx=max(max_indx,i+nums[i])
        return True