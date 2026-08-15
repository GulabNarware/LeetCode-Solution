class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indx=0
        for i in range(1,len(nums)):
            if nums[indx]!=nums[i]:
                indx+=1
                nums[indx]=nums[i]

        return indx+1

        
        