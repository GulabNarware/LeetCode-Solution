class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):

            if i!=0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                left=j+1
                right=n-1

                while left<right:
                    totalsum=nums[i]+ nums[j] + nums[left]+ nums[right]

                    if totalsum<target:
                        left+=1

                    elif totalsum>target:
                        right-=1

                    else:

                        temp=[nums[i],nums[j],nums[left],nums[right]]

                        res.append(temp)
                        left+=1
                        right-=1

                        while left<right and nums[left-1]==nums[left]:
                            left+=1

                        while left<right and nums[right+1]==nums[right]:
                            right-=1

        return res

                

            

