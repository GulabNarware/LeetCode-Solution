class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        n=len(nums)
        res=[]

        for first in range(n):
            if first!=0 and nums[first-1]==nums[first]:
                continue
            for second in range(first+1,n):
                if second-1!=first and nums[second-1] ==nums[second]:
                    continue
                third=second+1
                last=n-1
                while third<last:
                    temp= nums[first]+nums[second]+nums[third]+nums[last]
                    if temp<target:
                        third+=1
                    elif temp>target:
                        last-=1
                    else:
                        res.append([nums[first],nums[second],nums[third],nums[last]])
                        third+=1
                        last-=1
                        while third<last and nums[third-1]== nums[third]:
                            third+=1
                        while last>third and nums[last+1]==nums[last]:
                            last-=1

        return res




                

            

