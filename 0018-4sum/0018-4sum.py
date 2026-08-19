class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        result=[]

        n=len(nums)


        for first in range(n):

            if first!=0 and nums[first-1] == nums[first]:
                continue

            second=first+1

            for last in range(n-1,-1,-1):
                if last!=n-1 and nums[last+1]==nums[last]:
                   continue
                second=first+1
                third=last-1


                
                while second<third:
                    temp=nums[first]+nums[second]+nums[third]+nums[last]
                    if temp>target:
                        third-=1

                    elif temp<target:
                        second+=1

                    else:

                        result.append([nums[first],nums[second],nums[third],nums[last]])
                        
                        second+=1
                        third-=1

                        while nums[second]==nums[second-1] and second < third:
                            second+=1
                        while nums[third]==nums[third+1] and third>second:
                            third-=1
        return result
