class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        n=len(nums)
        result=[]

        for first in range(n):

            if first!=0 and nums[first]==nums[first-1]:
                continue

            second=first+1
            last=n-1

            while second <last:

                temp=nums[first]+nums[second]+nums[last]

                if temp>0:
                    last-=1

                elif temp<0:
                    second+=1

                else:
                    result.append([nums[first],nums[second],nums[last]])

                    last-=1
                    second+=1

                    while nums[second]==nums[second-1] and second<last:
                        second+=1

                    while nums[last]==nums[last+1] and last>second:
                        last-= 1
        return result




        