class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m=sum(nums)-(min(nums)*len(nums))

        return m