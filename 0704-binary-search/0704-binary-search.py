class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # left=0
        # right=len(nums)-1
        # while left <= right:
        #     mid =(left +right)//2
        #     if nums[mid]==target:
        #         return mid
        #     elif target<nums[mid]:
        #         right=mid-1
        #     elif target > nums[mid]:

        #         left=mid+1
        # return -1















        f=0
        l=len(nums)-1

        while f<= l:
            mid=(f+l)//2

            if nums[mid]==target:
                return mid

            if nums[mid]>target:
                l=mid-1

            else:
                f=mid+1

        return -1