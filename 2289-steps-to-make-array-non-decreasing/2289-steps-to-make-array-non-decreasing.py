class Solution:
    def totalSteps(self, nums: list[int]) -> int:

        #brute Force:-

        # count=0

        # while True :

        #     new=[]

        #     remove=False

        #     for i in range(len(nums)):
        #         if i>0 and nums[i-1]>nums[i]:
        #             remove=True

        #         else:
        #             new.append(nums[i])

        #     if not remove:
        #         return count

        #     count+=1
        #     nums=new

        # return count


        #Monotonic stack

        stack=[]
        ans=0
        for i in range(len(nums)-1,-1,-1):

            count=0

            while len(stack)>0 and stack[-1][0]<nums[i]:
                count=max(count+1,stack[-1][1])
                stack.pop()
            
            ans=max(ans,count)    
            stack.append((nums[i],count))

        return ans


            
            