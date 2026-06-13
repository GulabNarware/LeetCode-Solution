class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=[]
        
        i=0
        n=len(nums)
        nums.sort()

        for i in range(n):
            
            #skips the duplicate
            if i!=0 and nums[i]==nums[i-1]:
                continue

            #two pointer
            j=i+1
            k=n-1

            while j<k:

                totalsum=nums[i]+nums[j]+nums[k]

                if totalsum<0:
                    j+=1

                elif totalsum>0:
                    k-=1

                else:

                    temp=[nums[i],nums[j],nums[k]]
                    res.append(temp)

                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1

                    while k>j and nums[k]==nums[k+1]:
                        k-=1

        return res



