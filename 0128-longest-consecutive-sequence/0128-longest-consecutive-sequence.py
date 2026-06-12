class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # ln=0
        # d={}

        # for i in nums:
        #     d[i]=d.get(i,0)+1

        # for i in d:
        #     if i-1 not in d:
        #         length= 1

        #         while (i+length) in d:
        #             length+=1

        #         ln=max(length,ln)
        # return ln



        if len(nums)==0:
            return 0
        s=set(nums)
        ln=0
        
        for i in s:
            total=0
            if i-1 not in s:
                total=1
                while i+total in s:
                    total+=1

            ln=max(total,ln)
        return ln