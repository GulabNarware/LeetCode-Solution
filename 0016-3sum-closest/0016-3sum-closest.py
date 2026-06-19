class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ln=len(nums)

        res=nums[0]+nums[1]+nums[2]

        for first in range(ln):

            second ,last=first+1,ln-1

            while second < last:

                temp=nums[first]+nums[second]+nums[last]

                if abs(target-temp)< abs(target- res):
                    res=temp
                if temp < target :
                    second+=1
                elif temp> target:
                    last-=1
                else:
                    return temp

        return res




