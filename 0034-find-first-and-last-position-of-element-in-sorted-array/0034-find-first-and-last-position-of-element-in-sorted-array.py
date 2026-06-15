class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
     
        """
        LB=-1
        UB=-1
        res=[]

        left_lb=0
        right_lb=len(nums)-1

        while left_lb<= right_lb:

            mid=(left_lb+right_lb)//2
            if nums[mid]==target:
                LB=mid

            if nums[mid]>=target:
                right_lb=mid-1
            else:
                left_lb=mid+1
        left_ub=0
        right_ub=len(nums)-1

        while left_ub<=right_ub:
            mid=(left_ub+right_ub)//2
            if nums[mid]==target:
                UB=mid

            if nums[mid]>target:
                right_ub=mid-1
            else:
                left_ub=mid+1
        return [LB,UB]






     
















