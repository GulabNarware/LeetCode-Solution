class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        self.getchoice(nums,0,ans)

        return ans

    def getchoice(self,nums,indx,ans):

        if indx>=len(nums):
            ans.append(nums.copy())

            return 

        for i in range(indx,len(nums)):
            
            #Choice
            nums[i],nums[indx]=nums[indx],nums[i]

            #explore
            self.getchoice(nums,indx+1,ans)

            #Backtrack

            nums[i],nums[indx]=nums[indx],nums[i]





