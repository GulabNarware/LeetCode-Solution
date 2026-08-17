class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)

        lcs=0
        count=0

        for i in s:
            if i-1 not in s:
                count=1

                while i+count in s:
                    count+=1

                    lcs=max(count,lcs)

            # else:
            #     lcs=max(lcs,count)
            #     count=0

        lcs=max(lcs,count)

        return lcs
                