class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        positive_arr=[]
        negative_arr=[]

        res=[]

        for i in nums:
            if i>=0:
                positive_arr.append(i)

            else:
                negative_arr.append(i)

        for j in range(len(positive_arr)):
            res.append(positive_arr[j])
            res.append(negative_arr[j])

        return res