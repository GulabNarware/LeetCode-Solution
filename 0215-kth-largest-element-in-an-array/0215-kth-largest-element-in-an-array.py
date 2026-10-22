import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

# this is max heap with all writtern code:- O(n+nlogn)
        # ln=len(nums)

        # def heapDown(ln,arr,indx):

        #     larg=indx

        #     left=2*indx+1
        #     right=2*indx+2

        #     if left<ln and arr[left]>arr[larg]:
        #         larg=left

        #     if right<ln and arr[right]>arr[larg]:
        #         larg=right

        #     if larg!=indx:
        #         arr[larg],arr[indx]=arr[indx],arr[larg]

        #         heapDown(ln,arr,larg)


        # for i in range((ln//2)-1,-1,-1):
        #     heapDown(ln,nums,i)

        # for i in range(k-1):
        #     nums[0]=nums[-1]
        #     nums.pop()
        #     ln-=1
            
        #     heapDown(ln,nums,0)
        # return nums[0]

            
#using of min heap
        n=len(nums)
        pq=[]

        for i in range(k):
            heapq.heappush(pq,nums[i])

        for j in range(k,n):
            if nums[j]>pq[0]:
                
                heapq.heapreplace(pq,nums[j])

        return pq[0]