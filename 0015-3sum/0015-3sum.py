class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]

        nums.sort()

        n=len(nums)

        for first in range(len(nums)):

            if first!=0 and nums[first-1]==nums[first]:
                continue
        

            second=first+1

            last=n-1

            while second<last:
                
                
                temp_res=nums[first]+nums[second]+nums[last]
                if temp_res>0:
                    last-=1
                elif temp_res <0:
                    second+=1
                else:
                    temp=[nums[first],nums[second],nums[last]]

                    res.append(temp)

                    second+=1
                    last-=1

                    while nums[second-1]==nums[second] and second<last:
                        second+=1

                    while nums[last+1]==nums[last] and last>second:
                        last-=1
            
        return res
