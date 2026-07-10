# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lb=n

        left=0
        right=n

        while left<=right:
            mid=(left+right)//2

            if isBadVersion(mid):
                right=mid-1
                lb=mid
            else:
                left=mid+1

        return lb
