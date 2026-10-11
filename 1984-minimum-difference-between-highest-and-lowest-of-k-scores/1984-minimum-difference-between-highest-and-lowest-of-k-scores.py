class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if len(nums)==1 or len(nums)==0:
            return 0

        n=float('inf')
        nums.sort()
        left=0
        right=left+k-1
        while right<=len(nums)-1:
            m=nums[left]
            h=nums[right]
            if n> h-m :
                n=h-m
            left+=1
            right+=1

        return n