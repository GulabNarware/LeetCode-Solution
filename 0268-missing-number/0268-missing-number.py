class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        arr_sum=sum(nums)
        ln=len(nums)
        sum_ele=ln*(ln+1)//2


        return (ln*(ln+1)//2)-arr_sum
